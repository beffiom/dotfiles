-- Author: donmaiq
-- Appends url from clipboard to the playlist
-- Requires xclip(linux), powershell(windows), pbpaste(macOS)

-- detect_platform() and get_clipboard() copied and edited from:
    -- https://github.com/rossy/mpv-repl
    -- © 2016, James Ross-Gowan
    --
    -- Permission to use, copy, modify, and/or distribute this software for any
    -- purpose with or without fee is hereby granted, provided that the above
    -- copyright notice and this permission notice appear in all copies.

local platform = nil --set to 'linux', 'windows' or 'macos' to override automatic assign

if not platform then
  local o = {}
  if mp.get_property_native('options/vo-mmcss-profile', o) ~= o then
    platform = 'windows'
  elseif mp.get_property_native('options/input-app-events', o) ~= o then
    platform = 'macos'
  else
    platform = 'linux'
  end
end

local utils = require 'mp.utils'
local msg = require 'mp.msg'

--main function
function append(primaryselect)
  local clipboard = get_clipboard(primaryselect or false)
  if clipboard then
    mp.commandv("loadfile", clipboard, "append-play")
    local title = titleresolver(clipboard)
    mp.osd_message("Video Added!\n"..title)
    msg.info("Video Added!\n"..title)
  end
end

--handles the subprocess response table and return clipboard if it was a success
function handleres(res, args, primary)
  if not res.error and res.status == 0 then
      return res.stdout
  else
    --if clipboard failed try primary selection
    if platform=='linux' and not primary then
      append(true)
      return nil
    end
    msg.error("There was an error getting "..platform.." clipboard: ")
    msg.error("  Status: "..(res.status or ""))
    msg.error("  Error: "..(res.error or ""))
    msg.error("  stdout: "..(res.stdout or ""))
    msg.error("args: "..utils.to_string(args))
    return nil
  end
end

function get_clipboard(primary) 
  if platform == 'linux' then
    local args = { 'xclip', '-selection', primary and 'primary' or 'clipboard', '-out' }
    return handleres(utils.subprocess({ args = args }), args, primary)
  elseif platform == 'windows' then
    local args = {
      'powershell', '-NoProfile', '-Command', [[& {
        Trap {
          Write-Error -ErrorRecord $_
          Exit 1
        }
        $clip = ""
        if (Get-Command "Get-Clipboard" -errorAction SilentlyContinue) {
          $clip = Get-Clipboard -Raw -Format Text -TextFormatType UnicodeText
        } else {
          Add-Type -AssemblyName PresentationCore
          $clip = [Windows.Clipboard]::GetText()
        }
        $clip = $clip -Replace "`r",""
        $u8clip = [System.Text.Encoding]::UTF8.GetBytes($clip)
        [Console]::OpenStandardOutput().Write($u8clip, 0, $u8clip.Length)
      }]]
    }
    return handleres(utils.subprocess({ args =  args }), args)
  elseif platform == 'macos' then
    local args = { 'pbpaste' }
    return handleres(utils.subprocess({ args = args }), args)
  end
  return nil
end

mp.add_key_binding("P", "appendURL", append)

-- Added functionality: Send osd msg when a video is added to the playlist of a umpv instance
local file = mp.commandv('script-message', 'resolveurltitle', "arg[1]")

function umpv(file)
  mp.commandv("loadfile", file, "append-play")
  local title = titleresolver(file)
  mp.osd_message("Video Added!\n"..title)
  msg.info("Video Added!\n"..title)
end

function titleresolver(filename)
  local args = { 'youtube-dl', '--no-playlist', '--flat-playlist', '-sJ', filename }
  local res = utils.subprocess({ args = args })
  if res.status == 0 then
    local json, err = utils.parse_json(res.stdout)
    if not err then
      local is_playlist = json['_type'] and json['_type'] == 'playlist'
      local title = (is_playlist and '[playlist]: ' or '') .. json['title']
      return title
    end
  end
end

mp.register_script_message("appendUMPV", umpv)

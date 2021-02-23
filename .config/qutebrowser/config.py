#################################################################
# AUTOCONFIG
#################################################################
config.load_autoconfig()

################################################################
# GENERAL
#################################################################
## colors
colorBG = "#14161F"
colorBG2 = "#434758"
colorFG = "#bbc5ff"
colorError = "#f07178"
colorSuccess = "#c3e88d"
colorSelect = "#8b66a3"
colorSelect2 = "#c792ea"

## Set default startpage and default page
## [Url]
homePage = 'file:///home/shockman/.config/qutebrowser/local/startpage.html'

## Set the css theme
## [List of Urls]
theme = ["themes/darkstar.css"]

## Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## [Dict]
c.aliases = {
        'q':    'close',
        'qa':   'quit',
        'w':    'session-save',
        'wq':   'quit --save',
        'wqa':  'quit --save',
        }

## Time interval (in milliseconds) between auto-saves of config/cookies/etc.
## [Int]
c.auto_save.interval = 15000

## Always restore open sites when qutebrowser is reopened.
## [Bool]
c.auto_save.session = False

## Backend to use to display websites. qutebrowser supports two different web rendering engines / backends, QtWebKit and QtWebEngine. QtWebKit was discontinued by the Qt project with Qt 5.6, but picked up as a well maintained fork: https://github.com/annulen/webkit/wiki - qutebrowser only supports the fork. QtWebEngine is Qt’s official successor to QtWebKit. It’s slightly more resource hungry than QtWebKit and has a couple of missing features in qutebrowser, but is generally the preferred choice. This setting requires a restart.
## [String: webengine, webkit]
c.backend = 'webengine'

## Require a confirmation before quitting the application.
## [ConfirmQuit: always, multiple-tabs, downloads, never]
c.confirm_quit = ['downloads']

## Maximum time (in minutes) between two history items for them to be considered being from the same browsing session. Items with less time between them are grouped when being displayed in :history. Use -1 to disable separation.
## [Int]
c.history_gap_interval = 30

## Duration (in milliseconds) to show messages in the statusbar for. Set to 0 to never clear messages.
## [Int]
c.messages.timeout = 2000

#################################################################
# KEYBINDINGS
#################################################################

# Bindings for normal mode
config.unbind('d')
config.unbind('xo')
config.bind('m', 'hint links spawn umpv {hint-url}')
config.bind('M', 'quickmark-save')
config.bind('q', 'tab-close')
config.bind('cs', 'set-cmd-text :config-source')
config.bind('ce', 'config-edit')
config.bind(';', 'set-cmd-text :')
config.bind('t', 'config-cycle content.user_stylesheets themes/default.css themes/darkstar.css')
config.bind('di', 'hint images spawn wget -P Pictures {hint-url}')
config.bind('dl', 'hint links spawn wget -P Downloads {hint-url}')
config.bind('dv', 'hint links spawn youtube-dl --add-metadata -i -o "~/Videos/[%(uploader)s] %(title)s.%(ext)s" {hint-url}')
config.bind('da', 'hint links spawn youtube-dl --add-metadata -i -o "~/Music/%(title)s.%(ext)s" -x -f bestaudio/best {hint-url}')
config.bind('dt', 'hint links spawn wget -P .config/rtorrent/watch {hint-url}')
config.bind('gh', 'open ' + homePage)
config.bind('gH', 'open -t ' + homePage)
config.bind('pt', 'open -t -- {clipboard}')
config.bind('pw', 'open -w -- {clipboard}')
config.bind('yc', 'hint links yank')
config.bind('yi', 'hint images yank')
config.bind('=', 'zoom-in')
config.bind('+', 'zoom')
config.bind('pb', 'open -p ')
#config.bind('pw', 'spawn --userscript ~/.local/bin/programs/qute-keepass -p ~/.local/profile-5.kdbx')

#################################################################
# COLORS
#################################################################

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 ' + colorBG2 + ', stop:1 ' + colorBG + ')'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = colorBG

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = colorBG2

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = colorFG

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = colorSelect

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = colorSelect

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.item.selected.border.top = colorSelect

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = colorBG

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = colorFG

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 ' + colorSelect + ', stop:1 ' + colorSelect + ')'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = colorFG

# Font color for the matched part of hints.
# Type: QssColor
c.colors.hints.match.fg = colorSelect

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = colorFG

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = colorBG

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = colorBG

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = colorBG

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = colorBG

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '3px solid ' + colorSelect

# Background color of the statusbar in command mode
# Type: String
c.colors.statusbar.command.bg = colorBG

# Background color of the statusbar in normal mode
# Type: String
c.colors.statusbar.normal.bg = colorBG

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = colorSelect

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = colorSelect

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = colorSelect

# Background color of the statusbar in command mode
# Type: String
c.colors.statusbar.command.fg = colorFG

# Background color of the statusbar in normal mode
# Type: String
c.colors.statusbar.normal.fg = colorFG

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = colorFG

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = colorFG

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = colorFG

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = colorBG

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = colorFG

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = colorBG

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = colorFG

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = colorSelect2

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = colorSuccess

# Background color of the tab bar.
# Type: QtColor
c.colors.tabs.bar.bg = colorBG

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = colorError

# Color gradient start for: the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = colorBG

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = colorBG

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = colorBG2

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = colorBG

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = colorFG

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = colorSelect2

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = colorSelect

# Background color for webpages if unset (or empty to use the theme's
# color).
# Type: QtColor
c.colors.webpage.bg = colorBG

#################################################################
# COMPLETION
#################################################################

## Number of commands to save in the command history. 0: no history / -1: unlimited
## [Int]
c.completion.cmd_history_max_items = 10

## Delay (in milliseconds) before updating completions after typing a character
## [Int]
c.completion.delay = 0

## Height (in pixels or as percentage of the window) of the completion
## [Percent or Int]
c.completion.height = '20%'

## Minimum amount of characters needed to update completions
## [Int]
c.completion.min_chars = 1

## Move on to the next part when there’s only one possible completion left
## [Bool]
c.completion.quick = True

## Padding (in pixels) of the scrollbar handle in the completion window
c.completion.scrollbar.padding = 2

## Width (in pixels) of the scrollbar in the completion window
## [Int]
c.completion.scrollbar.width = 10

## When to show the autocompletion window
## [String: always (when available), auto (when requested), never
c.completion.show = 'always'

## Shrink the completion to be smaller than the configured size if there are no scrollbars
## [Bool]
c.completion.shrink = False

## Format of timestamps (e.g. for the history completion).
## See https://sqlite.org/lang_datefunc.html for allowed substitutions.
## [String]
c.completion.timestamp_format = '%Y-%m-%d'

## Execute the best-matching command on a partial match
## [Bool]
c.completion.use_best_match = False

## A list of patterns which should not be shown in the history. This only affects the completion. Matching URLs are still saved in the history (and visible on the qute://history page), but hidden in the completion. Changing this setting will cause the completion history to be regenerated on the next start, which will take a short while. This setting requires a restart.
## [UrlPattern] https://developer.chrome.com/apps/match_patterns
## c.completion.web_history.exclude =

## Number of URLs to show in the web history. 0: no history / -1: unlimited
## [Int]
c.completion.web_history.max_items = -1

#################################################################
# content
#################################################################

## Enable support for the HTML 5 web application cache feature. An application cache acts like an HTTP cache in some sense. For documents that use the application cache via JavaScript, the loader engine will first ask the application cache for the contents, before hitting the network.
## This setting supports URL patterns.
## This setting is only available with the QtWebKit backend.
## [Int]
## c.content.cache.appcache = True

## Maximum number of pages to hold in the global memory page cache. The page cache allows for a nicer user experience when navigating forth or back to pages in the forward/back history, by pausing and resuming up to n pages. For more information about the feature, please refer to: http://webkit.org/blog/427/webkit-page-cache-i-the-basics/
## This setting is only available with the QtWebKit backend.
## [Int]
## c.content.cache.maximum_pages = 0

## Size (in bytes) of the HTTP network cache. Null to use the default value. With QtWebEngine, the maximum supported value is 2147483647 (~2 GB).
## [Int]
## c.content.cache.size =

## Which cookies to accept.
##      - all: Accept all cookies.
##      - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
##      - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
##      - never: Don’t accept cookies at all.
## [String]
## c.content.cookies.accept = 'no-3rdparty'

## Store cookies.
## [Bool]
c.content.cookies.store = False

## Default encoding to use for websites. The encoding must be a string describing an encoding such as utf-8, iso-8859-1, etc.
## [Bool]
c.content.default_encoding = 'uft-8'

## Try to pre-fetch DNS entries to speed up browsing.
## This setting supports URL patterns.
## [Int]
## c.content.dns_prefetch = True

## Expand each subframe to its contents. This will flatten all the frames to become one scrollable page.
## This setting supports URL patterns.
## This setting is only available with the QtWebKit backend.
## [Bool]
## c.content.frame_flattening = False

## Allow websites to request geolocations.
## This setting supports URL patterns.
## [BoolAsk]
c.content.geolocation = False

## Value to send in the Accept-Language header. Note that the value read from JavaScript is always the global value.
## This setting supports URL patterns.
## [String]
c.content.headers.accept_language = 'en-US, us'

## Custom headers for qutebrowser HTTP requests.
## This setting supports URL patterns.
## [Dict]
## c.content.headers.custom =

## Value to send in the DNT header. When this is set to true, qutebrowser asks websites to not track your identity. If set to null, the DNT header is not sent at all.
## This setting supports URL patterns.
## [Bool]
c.content.headers.do_not_track = True

## When to send the Referer header. The Referer header tells websites from which website you were coming from when visiting them.
##      - always: Always send the Referer.
##      - never: Never send the Referer. This is not recommended, as some sites may break.
##      - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn’t break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
## [String]
## c.content.headers.referer = 'same-domain'

## Enable host blocking aka adblock.
## This setting supports URL patterns.
## [Bool]
c.content.blocking.enabled = False

## List of URLs of lists which contain hosts to block.
## The file can be in one of the following formats: An /etc/hosts-like file; One host per line; A zip-file of any of the above, with either only one file, or a file named hosts (with any extension).
## It’s also possible to add a local file or directory via a file:// URL. In case of a directory, all files in the directory are read as adblock lists.
## The file ~/.config/qutebrowser/blocked-hosts is always read if it exists.
## [List of Url]
c.content.blocking.hosts.lists = [
                    "file:///blocklist/",
                    "https://www.malwaredomainlist.com/hostslist/hosts.txt",
                    "https://someonewhocares.org/hosts/ipv6/hosts",
                    "http://winhelp2002.mvps.org/hosts.zip",
                    "http://malwaredomains.lehigh.edu/files/justdomains.zip",
                    "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext"]

## A list of patterns that should always be loaded, despite being ad-blocked. Note this whitelists blocked hosts, not first-party URLs. As an example, if example.org loads an ad from ads.example.org, the whitelisted host should be ads.example.org. If you want to disable the adblocker on a given page, use the content.host_blocking.enabled setting with a URL pattern instead. Local domains are always exempt from hostblocking.
## [List of UrlPattern]
## content.host_blocking.whitelist = "piwik.org"

## Enable hyperlink auditing (<a ping>).
## This setting supports URL patterns.
## [Bool]
c.content.hyperlink_auditing = False

## Load images automatically in web pages.
## This setting supports URL patterns.
## [Bool]
c.content.images = True

## Show javascript alerts.
# [Bool]
c.content.javascript.alert = False

## Allow JavaScript to read from or write to the clipboard. With QtWebEngine, writing the clipboard as response to a user interaction is always allowed.
## This setting supports URL patterns.
## [Bool]
c.content.javascript.can_access_clipboard = False

## Allow JavaScript to close tabs.
## This setting supports URL patterns.
## This setting is only available with the QtWebKit backend.
## [Bool]
## content.javascript.can_close_tabs = False

## Allow JavaScript to open new tabs without user interaction.
## This setting supports URL patterns.
## [Bool]
c.content.javascript.can_open_tabs_automatically = False

## Enable JavaScript.
## This setting supports URL patterns.
## [Bool]
c.content.javascript.enabled = True

# Enable JavaScript.
# [Bool]
# config.set('content.javascript.enabled', True, 'qute://*/*')

## Log levels to use for JavaScript console logging messages. When a JavaScript message with the level given in the dictionary key is logged, the corresponding dictionary value selects the qutebrowser logger to use. On QtWebKit, the "unknown" setting is always used.
## error: debug
## info: debug
## unknown: debug
## warning: debug
## [Dict]
c.content.javascript.log = {"unknown": "debug", "info": "debug", "warning": "debug", "error": "debug"}

## Use the standard JavaScript modal dialog for alert() and confirm().
## [Bool]
c.content.javascript.modal_dialog = False

## Show javascript prompts.
## [Bool]
c.content.javascript.prompt = True

## Allow locally loaded documents to access other local URLs.
## This setting supports URL patterns.
## [Bool]
c.content.local_content_can_access_file_urls = True

## Allow locally loaded documents to access remote URLs.
## This setting supports URL patterns.
## [Bool]
c.content.local_content_can_access_remote_urls = True

## Enable support for HTML 5 local storage and Web SQL.
## This setting supports URL patterns.
## [Bool]
c.content.local_storage = True

## Allow websites to record audio/video.
## This setting supports URL patterns.
## This setting is only available with the QtWebEngine backend.
## [BoolAsk]
# c.content.media_capture = False

## Netrc-file for HTTP authentication. If unset, ~/.netrc is used.
## [File]
## content.netrc_file =

## Allow websites to show notifications.
## [BoolAsk]
c.content.notifications = False

## Enable plugiZZns in Web pages.
## This setting supports URL patterns.
## [Bool]
c.content.plugins = False

## Draw the background color and images also when the page is printed.
## This setting supports URL patterns.
## [Bool]
# c.content.print_element_backgrounds = True

## Open new windows in private browsing mode which does not record visited pages.
## [Bool]
c.content.private_browsing = False

## Proxy to use. In addition to the listed values, you can use a socks://... or http://... URL.
## system: Use the system wide proxy.
## none: Don’t use any proxy
## [Proxy]
c.content.proxy = "system"

## Send DNS requests over the configured proxy.
## This setting is only available with the QtWebKit backend.
## [Bool]
# c.content.proxy_dns_requests = True

## Validate SSL handshakes.
## This setting supports URL patterns.
## [BoolAsk]
## c.content.ssl_strict = "Ask"

## List of user stylesheet filenames to use.
## [List of File, or File]
c.content.user_stylesheets = theme

## Exclude local files
## config.set('content.user_stylesheets', [], 'file:///*/*')

## Enable WebGL.
## This setting supports URL patterns.
## [Bool]
c.content.webgl = False

## Which interfaces to expose via WebRTC.
##      - all-interfaces: WebRTC has the right to enumerate all interfaces and bind them to discover public interfaces.
##      - default-public-and-private-interfaces: WebRTC should only use the default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
##      - default-public-interface-only: WebRTC should only use the default route used by http. This doesn’t expose any local addresses.
##      - disable-non-proxied-udp: WebRTC should only use TCP to contact peers or servers unless the proxy server supports UDP. This doesn’t expose any local addresses either.
## [String]
c.content.webrtc_ip_handling_policy = 'disable-non-proxied-udp'

## Limit fullscreen to the browser window (does not expand to fill the screen).
## [Bool]
c.content.fullscreen.window = False

## Monitor load requests for cross-site scripting attempts. Suspicious scripts will be blocked and reported in the inspector’s JavaScript console.
## This setting supports URL patterns.
## [Bool]
c.content.xss_auditing = True

#################################################################
# DOWNLOADS
#################################################################

## Directory to save downloads to. If unset, a sensible OS-specific default is used.
## [Directory]
c.downloads.location.directory = "~/Downloads"

## Prompt the user for the download location. If set to false, downloads.location.directory will be used.
## [Bool]
c.downloads.location.prompt = True

## Remember the last used download directory.
## [Bool]
c.downloads.location.remember = False

## What to display in the download filename input.
##      - path: Show only the download path.
##      - filename: Show only download filename.
##      - both: Show download path and filename.
## [String]
c.downloads.location.suggestion = "filename"

## Default program used to open downloads. If null, the default internal handler is used. Any {} in the string will be expanded to the filename, else the filename will be appended.
## [String]
## downloads.open_dispatcher =

## Where to show the downloaded files.
## [VerticalPosition: top, bottom]
c.downloads.position = "bottom"

## Duration (in milliseconds) to wait before removing finished downloads. If set to -1, downloads are never removed
## [Int]
c.downloads.remove_finished = 5000

#################################################################
# EDITOR
#################################################################

## Editor (and arguments) to use for the open-editor command. The following placeholders are defined: * {file}: Filename of the file to be edited. * {line}: Line in which the caret is found in the text. * {column}: Column in which the caret is found in the text. * {line0}: Same as {line}, but starting from index 0. * {column0}: Same as {column}, but starting from index 0.
## [ShellCommand]
c.editor.command = ["$TERMINAL -e $EDITOR", "-f", "{file}", "-c", "normal {line}G{column0}l"]

## Encoding to use for the editor.
## [Encoding]
c.editor.encoding = "utf-8"

#################################################################
# FONTS
#################################################################

## Font used in the completion categories.
## [Font]
c.fonts.completion.category = 'bold 12pt monospace'

## Font used in the completion widget.
## [Font]
c.fonts.completion.entry = '12pt monospace'

## Font used for the debugging console.
## [QtFont]
c.fonts.debug_console = '12pt monospace'

## Font used for the downloadbar.
## [Font]
c.fonts.downloads = '12pt monospace'

## Font used for the hints.
## [Font]
c.fonts.hints = 'bold 12pt monospace'

## Font used in the keyhint widget.
## [Font]
c.fonts.keyhint = '12pt monospace'

## Font used for error messages.
## [Font]
c.fonts.messages.error = '12pt monospace'

## Font used for info messages.
## [Font]
c.fonts.messages.info = '12pt monospace'

## Font used for warning messages.
## [Font]
c.fonts.messages.warning = '12pt monospace'

## Default monospace fonts. Whenever "monospace" is used in a font setting, it’s replaced with the fonts listed here.
## [Font]
## c.fonts.monospace = 'monospace'

## Font used for prompts.
## [Font]
c.fonts.prompts = '12pt monospace'

## Font used in the statusbar.
## [Font]
c.fonts.statusbar = 'bold 14pt monospace'

## Font used in the tab bar.
## [QtFont]
c.fonts.tabs.selected = 'bold 16pt monospace'
c.fonts.tabs.unselected = 'bold 12pt monospace'

## Font family for cursive fonts.
## [FontFamily]
## c.fonts.web.family.cursive =

## Font family for fantasy fonts.
## [FontFamily]
## c.fonts.web.family.fantasy =

## Font family for fixed fonts.
## [FontFamily]
## c.fonts.web.family.fixed =

## Font family for sans-serif fonts.
## [FontFamily]
## c.fonts.web.family.sans_serif =

## Font family for serif fonts.
## [FontFamily]
## c.fonts.web.family.serif =

## Font family for standard fonts.
## [FontFamily]
## c.fonts.web.family.standard =

## Default font size (in pixels) for regular text.
## [Int]
c.fonts.web.size.default = 20

## Default font size (in pixels) for fixed-pitch text.
## [Int]
c.fonts.web.size.default_fixed = 15

## Hard minimum font size (in pixels).
## [Int]
c.fonts.web.size.minimum = 0

## Minimum logical font size (in pixels) that is applied when zooming out.
## [Int]
c.fonts.web.size.minimum_logical = 10

#################################################################
# HINTS
#################################################################

## When a hint can be automatically followed without pressing Enter.
##      - always: Auto-follow whenever there is only a single hint on a page.
##      - unique-match: Auto-follow whenever there is a unique non-empty match in either the hint string (word mode) or filter (number mode).
##      - full-match: Follow the hint when the user typed the whole hint (letter, word or number mode) or the element’s text (only in number mode).
##      - never: The user will always need to press Enter to follow a hint.
## [String]
c.hints.auto_follow = 'unique-match'

## Duration (in milliseconds) to ignore normal-mode key bindings after a successful auto-follow.
## [Int]
c.hints.auto_follow_timeout = 0

## CSS border value for hints.
## [String]
c.hints.border = '2px solid ' + colorBG

## Characters used for hint strings.
## [UniqueCharString]
c.hints.chars = 'asdfghjkl'

## Dictionary file to be used by the word hints.
## [File]
c.hints.dictionary = '/usr/share/dict/words'

## Which implementation to use to find elements to hint.
## This setting is only available with the QtWebKit backend.
##      - javascript: Better but slower
##      - python: Slightly worse but faster
## [String]
## c.hints.find_implementation = 'python'

## Hide unmatched hints in rapid mode.
## [Bool]
c.hints.hide_unmatched_rapid_hints = True

## Minimum number of characters used for hint strings.
## [Int]
c.hints.min_chars = 1

## Mode to use for hints.
##      - number: Use numeric hints. (In this mode you can also type letters from the hinted element to filter and reduce the number of elements that are hinted.)
##      - letter: Use the characters in the hints.chars setting.
##      - word: Use hints words based on the html elements and the extra words.
## [String]
c.hints.mode = 'letter'

## Comma-separated list of regular expressions to use for next links.
## [List of Regex]
## c.hints.next_regexes =

## Comma-separated list of regular expressions to use for prev links.
## [List of Regex]
## c.hints.prev_regexes =

## Scatter hint key chains (like Vimium) or not (like dwb). Ignored for number hints.
## [Bool]
c.hints.scatter = True

## CSS selectors used to determine which elements on a page should have hints.
## This setting supports URL patterns.
## This setting can only be set in config.py.
## c.hints.selectors =

## Make characters in hint strings uppercase.
## [Bool]
c.hints.uppercase = False

#################################################################
# INPUT
#################################################################

## Which unbound keys to forward to the webview in normal mode.
##      - all: Forward all unbound keys.
##      - auto: Forward unbound non-alphanumeric keys.
##      - none: Don’t forward any keys.
## [String]
c.input.forward_unbound_keys = 'auto'

## Leave insert mode if a non-editable element is clicked.
## [Bool]
c.input.insert_mode.auto_leave = True

## Automatically enter insert mode if an editable element is focused after loading the page.
## [Bool]
c.input.insert_mode.auto_load = False

## Switch to insert mode when clicking flash and other plugins.
## [Bool]
c.input.insert_mode.plugins = False

## Include hyperlinks in the keyboard focus chain when tabbing.
## This setting supports URL patterns.
c.input.links_included_in_focus_chain = True

## Timeout (in milliseconds) for partially typed key bindings. If the current input forms only partial matches, the keystring will be cleared after this time.
## [Int]
c.input.partial_timeout = 5000

## Enable Opera-like mouse rocker gestures. This disables the context menu.
## [Bool]
c.input.mouse.rocker_gestures = False

## Enable spatial navigation. Spatial navigation consists in the ability to navigate between focusable elements in a Web page, such as hyperlinks and form controls, by using Left, Right, Up and Down arrow keys. For example, if the user presses the Right key, heuristics determine whether there is an element he might be trying to reach towards the right and which element he probably wants.
## This setting supports URL patterns.
## [Bool]
c.input.spatial_navigation = False

#################################################################
# KEYHINT
#################################################################

## Keychains that shouldn’t be shown in the keyhint dialog. Globs are supported, so ;* will blacklist all keychains starting with ;. Use * to disable keyhints.
## [List of String]
## c.keyhint.blacklist =

## Time (in milliseconds) from pressing a key to seeing the keyhint dialog.
## [Int]
c.keyhint.delay = 500

## Rounding radius (in pixels) for the edges of the keyhint dialog.
## [Int]
c.keyhint.radius = 45

#################################################################
# NEW INSTANCE
#################################################################

## How to open links in an existing instance if a new one is launched. This happens when e.g. opening a link from a terminal. See new_instance_open_target_window to customize in which window the link is opened in.
##      - tab: Open a new tab in the existing window and activate the window.
##      - tab-bg: Open a new background tab in the existing window and activate the window.
##      - tab-silent: Open a new tab in the existing window without activating the window.
##      - tab-bg-silent: Open a new background tab in the existing window without activating the window.
##      - window: Open in a new window.
## [String]
c.new_instance_open_target = 'tab-bg-silent'

## Which window to choose when opening links as new tabs. When new_instance_open_target is set to window, this is ignored.
##      - first-opened: Open new tabs in the first (oldest) opened window.
##      - last-opened: Open new tabs in the last (newest) opened window.
##      - last-focused: Open new tabs in the most recently focused window.
##      - last-visible: Open new tabs in the most recently visible window.
## [String]
c.new_instance_open_target_window = 'last-focused'

#################################################################
# PROMPT
#################################################################

## Show a filebrowser in upload/download prompts.
## [Bool]
c.prompt.filebrowser = False

## Rounding radius (in pixels) for the edges of prompts.
## [Int]
c.prompt.radius = 45

#################################################################
# SCROLLING
#################################################################

## Show the scrollbar.
## [String]
c.scrolling.bar = 'never'

## Enable smooth scrolling for web pages. Note smooth scrolling does not work with the :scroll-px command.
## This setting supports URL patterns.
## [Bool]
c.scrolling.smooth = True

#################################################################
# SEARCH
#################################################################

## When to find text on a page case-insensitively.
##      - always: Search case-insensitively.
##      - never: Search case-sensitively.
##      - smart: Search case-sensitively if there are capital characters.
## [IgnoreCase]
c.search.ignore_case = 'smart'

## Find text on a page incrementally, renewing the search for each typed character.
## [Bool]
c.search.incremental = True

#################################################################
# session
#################################################################

## Name of the session to save by default. If this is set to null, the session which was last loaded is saved.
## [SessionName]
## c. session.default_name =

## Load a restored tab as soon as it takes focus.
## [Bool]
c.session.lazy_restore = False

#################################################################
# SPELLCHECK
#################################################################

## Languages to use for spell checking. You can check for available languages and install dictionaries using scripts/dictcli.py. Run the script with -h/--help for instructions.
## On QtWebKit, this setting is unavailable.
## [List of String]
## spellcheck.languages = {'en-US', 'fr-Fr'}

#################################################################
# STATUSBAR
#################################################################

## Hide the statusbar unless a message is shown.
## [String]
c.statusbar.show = 'in-mode'

## Padding (in pixels) for the statusbar.
## [Padding]
c.statusbar.padding = {"top": 2, "bottom": 2, "left": 1, "right": 1}

## Position of the status bar.
## [VerticalPosition]
c.statusbar.position = 'bottom'

#################################################################
# TABS
#################################################################

## Open new tabs (middleclick/ctrl+click) in the background.
## [Bool]
c.tabs.background = True

## Mouse button with which to close tabs.
##      - right: Close tabs on right-click.
##      - middle: Close tabs on middle-click.
##      - none: Don’t close tabs using the mouse.
## [String]
c.tabs.close_mouse_button = 'middle'

## How to behave when the close mouse button is pressed on the tab bar.
##      - new-tab: Open a new tab.
##      - close-current: Close the current tab.
##      - close-last: Close the last tab.
##      - ignore: Don’t do anything.
## [String]
c.tabs.close_mouse_button_on_bar = 'new-tab'


## Scaling factor for favicons in the tab bar. The tab size is unchanged, so big favicons also require extra tabs.padding.
## [Float]
c.tabs.favicons.scale = 1.0

## When to show favicons in the tab bar.
## [Bool]
# c.tabs.favicons.show = True

## Padding (in pixels) for tab indicators.
## [Padding]
c.tabs.indicator.padding = {"top": 0, "bottom": 0, "left": 0, "right": 5}

## Width (in pixels) of the progress indicator (0 to disable).
## [Int]
c.tabs.indicator.width = 2

## How to behave when the last tab is closed.
##      - ignore: Don’t do anything.
##      - blank: Load a blank page.
##      - startpage: Load the start page.
##      - default-page: Load the default page.
##      - close: Close the window.
## [String]
c.tabs.last_close = 'close'

## Switch between tabs using the mouse wheel.
## [Bool]
c.tabs.mousewheel_switching = True

## Position of new tabs opened from another tab. See tabs.new_position.stacking for controlling stacking behavior.
##      - prev: Before the current tab.
##      - next: After the current tab.
##      - first: At the beginning.
##      - last: At the end.
## [NewTabPosition]
c.tabs.new_position.related = 'next'

## Position of new tabs which are not opened from another tab. See tabs.new_position.stacking for controlling stacking behavior.
##      - prev: Before the current tab.
##      - next: After the current tab.
##      - first: At the beginning.
##      - last: At the end.
## [NewTabPosition]
c.tabs.new_position.unrelated = 'next'

## Padding (in pixels) around text for tabs.
## [Padding]
c.tabs.padding = {"top": 0, "bottom": 0, "left": 0, "right": 0}

## Shrink pinned tabs down to their contents.
## [Bool]
c.tabs.pinned.shrink = True

## Position of the tab bar.
## [Position: top, bottom, left, right]
c.tabs.position = 'top'

## Which tab to select when the focused tab is removed.
##      - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
##      - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
##      - last-used: Select the previously selected tab.
## [SelectOnRemove]
c.tabs.select_on_remove = 'prev'

## When to show the tab bar.
##      - always: Always show the tab bar.
##      - never: Always hide the tab bar.
##      - multiple: Hide the tab bar if only one tab is open.
##      - switching: Show the tab bar when switching tabs.
## [String]
c.tabs.show = 'multiple'

## Duration (in milliseconds) to show the tab bar before hiding it when tabs.show is set to switching.
## [Int]
c.tabs.show_switching_delay = 3000

## Open a new window for every tab.
## [Bool]
c.tabs.tabs_are_windows = False

## Alignment of the text inside of tabs.
## [TextAlignmen: left, right, center]
c.tabs.title.alignment = 'center'

## Format to use for the tab title. The following placeholders are defined:
##      - {perc}: Percentage as a string like [10%].
##      - {perc_raw}: Raw percentage, e.g. 10.
##      - {current_title}: Title of the current web page.
##      - {title_sep}: The string ` - ` if a title is set, empty otherwise.
##      - {index}: Index of this tab.
##      - {id}: Internal tab ID of this tab.
##      - {scroll_pos}: Page scroll position.
##      - {host}: Host of the current web page.
##      - ‘{backend}`: Either 'webkit’ or 'webengine'
##      - {private}: Indicates when private mode is enabled.
##      - {current_url}: URL of the current web page.
##      - {protocol}: Protocol (http/https/…) of the current web page.
##      - {audio}: Indicator for audio/mute status.
## [FormatString]
c.tabs.title.format = '{private}{current_title}'

## Format to use for the tab title for pinned tabs. The same placeholders like for tabs.title.format are defined.
## [FormatString]
c.tabs.title.format_pinned = None

## Width (in pixels or as percentage of the window) of the tab bar if it’s vertical.
## [PercOrInt]
c.tabs.width = 35

## Wrap when changing tabs.
## [Bool]
c.tabs.wrap = True

#################################################################
# UBLOCK
#################################################################
import sys, os
sys.path.append(os.path.join(sys.path[0], 'jmatrix'))
config.source("jmatrix/jmatrix/integrations/qutebrowser.py")

#################################################################
# URL
#################################################################

## What search to start when something else than a URL is entered.
##      - naive: Use simple/naive check.
##      - dns: Use DNS requests (might be slow!).
##      - never: Never search automatically.
## [String]
c.url.auto_search = 'naive'

## Page to open if :open -t/-b/-w is used without URL. Use about:blank for a blank page.
## [FuzzyUrl]
## c.url.default_page = homePage

## URL segments where :navigate increment/decrement will search for a number.
## [FlagList: host, port, path, query, anchor]

## Open base URL of the searchengine if a searchengine shortcut is invoked without parameters.
## [Bool]
c.url.open_base_url = True

## Search engines which can be used via the address bar. Maps a search engine name (such as DEFAULT, or ddg) to a URL with a {} placeholder. The placeholder will be replaced by the search term, use {{ and }} for literal {/} signs. The search engine named DEFAULT is used when url.auto_search is turned on and something else than a URL was entered to be opened. Other search engines can be used by prepending the search engine name to the search term, e.g. :open google qutebrowser.
## [Dict]
c.url.searchengines = {"DEFAULT": "https://duckduckgo.com/?q={}",
        's':     'https://searx.ninja/?q={}',
        'w':       'https://en.wikipedia.org/wiki/{}',
        'v':       'https://invidious.snopyta.org/search?q={}',
        'i':       'https://searx.ninja/?q=!images+{}',
        'tw':      'https://nitter.snopyta.org/{}',
        'tws':      'https://nitter.snopyta.org/search?f=tweets&q={}&since=&until=&near=',
        '4':       'https://4channel.org/{}/catalog',
        }

## Page(s) to open at the start.
## [List of FuzzUrl, or FuzzyUrl]
c.url.start_pages = homePage

## URL parameters to strip with :yank url.
## [List of String]
## c.url.yank_ignored_parameters = {'ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'}

#################################################################
# WINDOW
#################################################################

## Hide the window decoration.
## [Bool]
## c.window.hide_decoration = True

## Format to use for the window title. The same placeholders like for tabs.title.format are defined.
## [FormatString]
## c.window.title_format = '{perc}{current_title}{title_sep}qutebrowser'

#################################################################
# ZOOM
#################################################################

## Default zoom level.
## [Perc]
c.zoom.default = '125%'

## Available zoom levels.
## [List of Perc]
## c.zoom.levels = {25, 33, 50, 67, 75, 90, 100, 110, 125, 150, 175, 200, 250, 300, 400, 500}

## Number of zoom increments to divide the mouse wheel movements to.
## [Int]
c.zoom.mouse_divider = 512

## Apply the zoom factor on a frame only to the text or to all content.
## This setting supports URL patterns.
## This setting is only available with the QtWebKit backend.
## [Bool]
## c.zoom.text_only = False

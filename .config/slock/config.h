/* user and group to drop privileges to */
static const char *user  = "nobody";
static const char *group = "wheel";

static const char *colorname[NUMCOLS] = {
	[INIT] =   "#14161F",     /* after initialization */
	[INPUT] =  "#434758",   /* during input */
	[FAILED] = "#f07178",   /* wrong password */
};

/* treat a cleared input like a wrong password (color) */
static const int failonclear = 0;

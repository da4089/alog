//


#include <X11/Intrinsic.h>


int
main(
    int argc,
    char *argv[])
{
    XtAppContext context;
    Widget toplevel;

    XtSetLanguageProc(NULL, NULL, NULL);

    toplevel = XtAppInitialize(&context,
                               "ALog",
                               NULL,
                               0,
                               &argc,
                               argv,
                               NULL,
                               NULL,
                               0);

    return 0;
}

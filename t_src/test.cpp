#include <ncurses.h>
#include "libtuiframes.h"
bool break_=false;
int main()
{	int ch;

	initscr();			/* Start curses mode 		*/
	raw();				/* Line buffering disabled	*/
	keypad(stdscr, TRUE);		/* We get F1, F2 etc..		*/
	noecho();			/* Don't echo() while we do getch */

    	printw("Type any character to see it in bold\n");

	while(!break_)
	{
		ch = getch();
		if(ch == 'q')
		{
			printw("F1 Key pressed");

			break_=true;
		}
		else
		{	printw("The pressed key is ");
			attron(A_BOLD);
			printw("%c", ch);
			attroff(A_BOLD);
		}
		refresh();			/* Print it on to the real screen */
	}
	
	endwin();			/* End curses mode		  */

	return 0;
}

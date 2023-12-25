#include "libtuiframes.h"
namespace tui
{
	tuiWindows::tuiWindows(FrameRatio_t frameRatio_x)
	{
		frameRatio=frameRatio_x;
	}

	FrameSize_t tuiWindows::getSize(void)
	{
		FrameSize_t ret={0,0};
		return ret;
	}
	
	void tuiWindows::initFrame(void)
	{
		initscr();
	}
	void * tuiWindows::drawFrame(void * ptr)
	{
		
	}
};

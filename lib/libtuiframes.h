#include<stdio.h>
#include<pthread.h>
#include<ncurses.h>
#include<stdint.h>
namespace tui
{
	typedef uint8_t FrameDim_t;
	typedef uint8_t Return_t;
	
	typedef enum
	{
		StdOK,
		StdNOK
	}Return_enm;


	typedef struct FrameRatio_t
	{
		FrameDim_t Height;
		FrameDim_t Width;
	};
	typedef FrameRatio_t FrameSize_t;
	typedef class tuiWindows
	{
		public:
		FrameSize_t frameSize;
		FrameRatio_t frameRatio;
		tuiWindows(FrameRatio_t);

		private:
		void initFrame(void);
		FrameSize_t getSize(void);
		void * drawFrame(void * ptr);
		void * ctrlFrame(void * ptr);
	};
};

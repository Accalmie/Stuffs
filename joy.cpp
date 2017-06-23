#include <windows.h>

int main(){

	DWORD DO = 261.626;
	DWORD RE = 293.665;
	DWORD MI = 329.628;
	DWORD FA = 349.228;
	DWORD SOL = 391.995;
	DWORD LA = 440.000;
	DWORD SI = 493.883;
	DWORD DO_UP = 523.251;
	DWORD RE_UP = 587.330;

	DWORD hymn[] = {SI, SI, DO_UP, RE_UP, RE_UP, DO_UP, SI, LA, SOL, SOL, LA, SI, SI, LA, LA, SI, SI, DO_UP, RE_UP, RE_UP, DO_UP, SI, LA, SOL, SOL, LA, SI, LA, SOL, SOL,
		LA, LA, SI, SOL, LA, SI, DO_UP, SI, SOL, LA, SI, DO_UP, SI, LA, SOL, LA , RE, SI, SI, DO_UP, RE_UP, RE_UP, DO_UP, SI, LA, SOL, SOL, LA, SI, LA, SOL, SOL};

	for (i = 0; i < sizeof(hymn)/sizeof(*hymn); i++){
		if (i == 13 || i == 60 || i == 41 || i == 40 || i == 36 || i == 35 || i == 28)
			Beep(hymn[i], 250);
		else if (i == 12 || i == 27 || i == 59)
			Beep(hymn[i], 750);
		else if (i == 14 || i == 29 || i == 61){
			Beep(hymn[i], 900);
			Sleep(100);
		}
		else
			Beep(hymn[i], 500);
	}
}
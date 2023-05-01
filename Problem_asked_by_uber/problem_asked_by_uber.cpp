#include <iostream>

int main()
{

	int input_array[] = {1, 2, 3, 4, 5};
	int array_size = sizeof(input_array)/sizeof(int);
	int* output_array = new int[array_size];
	int temp_val = 1;

	for (int i = 0; i < array_size; i++)
	{
		for (int j = 0; j<array_size; j++) {
			if (j != i)
			{
				temp_val *= input_array[j];
			}
		}
		output_array[i] = temp_val;
		temp_val = 1;
	}

	for (int i = 0; i <= array_size; i++)
	{
		if (i==0)
		{
			std::cout<<"["<<output_array[i];
		}
		else if (i>0 && i<array_size)
		{
			std::cout<<","<<output_array[i];
		}
		else
		{
			std::cout<<"]"<<std::endl;
		}
	}
	return 0;
}

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;


int main()
{
	string fname = "dwarf_family_tree.csv";



 
	vector<vector<string>> content;
	vector<string> row;
	string line, word;
 
	fstream file (fname, ios::in);
  ofstream outfile("output.dot");
  outfile << "digraph G {" << endl;

  outfile << "Rankdir = LR" << endl;

  outfile << "-1 [label = start]" << endl;


  
	if(file.is_open())
	{
		while(getline(file, line))
		{
			row.clear();
 
			stringstream str(line);
 
			while(getline(str, word, ','))
				row.push_back(word);
			content.push_back(row);
		}
	}
	else
		cout<<"Could not open the file\n";
  file.close();

  
  ifstream infile("asian_surnames.txt");

  string names [57];
  int x = 0;
  while (!infile.eof())
    {
        infile >> names[x];
          x++;
    }

  x = 0;
  for(int i=1;i<content.size();i++)
	{
		for(int j=0;j<content[i].size();j++)
		{
      
			if(j == 0)
      { 
    
          if(x == 56)
            x = 0;
         outfile << content[i][0] << " [label =  "<< names[x];
        x++;
        
        
     // 
      }
      if (j == 2)
        if(content[i][2] == "M")
            outfile << ", color = Blue, shape = rectangle]" << endl;
        else
          outfile << ", color = Pink, shape = rectangle]" << endl;
     
		}
    
	}
outfile << endl;
  
  for(int i=1;i<content.size();i++)
	{
    
    if(content[i][11] != "")
    {
      outfile << "{rank = same" << endl;
      outfile << content[i][11] <<"," << content[i][0];
      outfile << "}" << endl;
    }
   
    //generation
   
      
  
    outfile << content[i][14] << "-> " << content[i][0];
    outfile << " [dir = none]" << endl;
   //finds parent for child
  }
 
  outfile << "}";
  outfile.close();
  
	return 0;
}

 

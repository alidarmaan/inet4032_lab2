 #!/bin/bash
              
              a=2
              b=2
              c=$((a + b))
              
              echo "Bash says: Hello, World!"
              echo "$a + $b = $c"
	      
              declare -a myList=("User1" "User2" "User3")
              for user in "${myList[@]}"
              do
                      echo "$user"
              done

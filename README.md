# Digital-Image-Processing-For-Cyber-Security

The Extracting Metadata from Digital Images .py file requests a user to enter a path to a directory containing jpeg files. Using that path, it processes all the .jpg files contained in that folder to extract the GPS Coordinates for each jpg (if it exists).

The Processing Digital Images .py file prompts the user for a directory path to search and verify that the path provided exists. Then it iterates through each file in that directory and examines the images in that directory using the PIL Python module. Finally, it generate a prettytable report of the search results (sample shown here)

+---------------------------------------------------------------+
| File                  | Ext  | Format | Width | Height | Mode |
+---------------------------------------+------+--------+-------+
| .\photos\PH01236U.BMP | .BMP | BMP    | 216    | 143   | P |
| .\photos\PH02039U.BMP | .BMP | BMP    | 216    | 143   | P |
| .\photos\PH02752U.BMP | .BMP | BMP    | 216    | 142   | P |
| .\photos\38467giu.gif | .gif | GIF    | 300    | 212   | P |
| .\photos\AG00004_.GIF | .GIF | GIF    | 140    | 135   | P |

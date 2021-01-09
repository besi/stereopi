width = 100;
depth = 56;
height = 32;
gap = 1; // Gap between the board due to the 1mm screen connector

module hole(index){
    offsetx = 7;
    offsety = 5.5;
    r = 2;
    hole_distance = 5;
    
    translate([gap + offsetx + (index * 5), depth - offsety])
        linear_extrude(height)
            circle(r, $fn = 50);
    
}



module main(){
difference()
{
    cube([ width, depth, height ]);
    hole(0);
        hole(1);
        hole(2);
        hole(3);
        hole(4);
        hole(5);
}    
    }
  

main();
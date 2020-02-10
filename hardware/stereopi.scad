DXF = true; // set to true to see the DXF projection, for a laser cutter for
            // example

file = "makercase-50-30-105-inside-3-5mm-thickness.dxf";
thickness = 3.5;

inner_width = 50;
inner_height = 30;
inner_depth = 105;

outer_width = inner_width + 2 * thickness;
outer_height = inner_height + 2 * thickness;
outer_depth = inner_depth + 2 * thickness;

spacing = 6;

module dxf(layer)
{
    import(file = "makercase-50-30-105-inside-3-5mm-thickness.dxf",
           layer = layer);
}

module
back()
{
    linear_extrude(height = thickness, center = true) difference()
    {
        dxf("back_outsideCutPath", 0); // , - outer_height - spacing
        plug_radius = 3.5;
        translate([
            outer_width / 2,
            outer_height + spacing / 2 * 2 + outer_height / 2
        ]) circle(plug_radius, $fn = 20);
    }
}

module
top()
{
    offset_x = outer_depth + outer_width + 1 * spacing;
    offset_y = spacing / 2;
    linear_extrude(height = thickness, center = true)

        difference()
    {

        dxf("top_outsideCutPath", 0);

        translate([ offset_x + (outer_width / 2) + 15, offset_y + 50 ])
            rotate(90) text("StereoPi");
    }
}

module
front()
{

    socket_width = 7.5;
    chip_height = 12;

    linear_extrude(height = thickness, center = true) difference()
    {
        dxf("front_outsideCutPath", 0);

        // Microusb
        chip_width = 17;
        chip_offset = 12.5;
        translate([
            outer_width - chip_width / 2 - chip_offset,
            spacing / 2 +
            chip_height
        ]) square([ chip_width, 1 ], center = true);
        translate([
            outer_width - chip_width / 2 - chip_offset,
            spacing / 2 + chip_height + 1.5
        ]) square([ socket_width, 3 ], center = true);

        // Switch
        switch_height = 25;
        switch_radius = 3;
        translate([
            outer_width - chip_width / 2 - chip_offset,
            spacing / 2 +
            switch_height
        ]) circle(switch_radius, $fn = 50);

        // Charging indicator
        charging_radius = .8;
        translate([
            outer_width - chip_width - chip_offset + 1,
            spacing / 2 + chip_height + 4
        ]) circle(charging_radius, $fn = 20);
    }
}

module
left()
{

    linear_extrude(height = thickness, center = true) difference()
    {
        dxf("left_outsideCutPath", 0);
    }
}

module
right()
{
    linear_extrude(height = thickness, center = true)
        dxf("right_outsideCutPath", 0);
}

module
bottom()
{
    linear_extrude(height = thickness, center = true)
        dxf("bottom_outsideCutPath", 0);
}

module
box()
{
    front();
    back();
    right();
    left();
    bottom();
    top();
}

if (DXF) {
    projection(cut = true) box();
} else {
    box();
}
%Load the Korea data grid and the land area boundary.
load korea
S = shaperead('landareas','UseGeoCoords',true);

%Create a worldmap and project and display the Korea data grid as a texture map.
figure
worldmap(map, refvec)
geoshow(map, refvec,'DisplayType','texturemap')
demcmap(map)
axis off
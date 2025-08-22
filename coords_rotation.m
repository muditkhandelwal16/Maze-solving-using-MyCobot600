filename = 'robot_path.csv';
data = readmatrix(filename);
disp(data)
data_len=length(data);
coords=zeros(data_len,3);

function a=coord(coords,len,the)
    the=the*pi/180;
    rotation=[cos(the) -sin(the) 0;sin(the) cos(the) 0;0 0 1];
    for i=1:len
        coords(i,:)=rotation*[coords(i,1)-17 coords(i,2)-17 coords(1,3)]';
    end
    disp(coords)
end
for i=1:data_len
    X_mm=data(i,1);
    Y_mm=data(i,2);
    Z_mm=0.1;
    coords(i,:)=[X_mm Y_mm Z_mm];
end
coord(coords,data_len,90)
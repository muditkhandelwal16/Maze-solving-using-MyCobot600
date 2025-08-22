python_command = 'python A_star_maze_solver.py';

% Run the Python script from MATLAB
[status, cmdout] = system(python_command);
% deg = str2double(cmdout);

filename = 'robot_path.csv';
data = readmatrix(filename);
disp(data)
data_len=length(data);
coords=zeros(data_len,3);

startpos = [30 -130.20 -128.53 -11.27 90.00 1.38]*pi/180;

robot_x=400;
robot_y=150;

for i=1:data_len
    X_mm=(-data(i,1)*4.62-robot_x)/1000; %coordinates are swapt 0,12 is now 12,0
    Y_mm=(-data(i,2)*4.62-robot_y)/1000; % because here this is y,x ---->   x,y
    Z_mm=0.1;
    coords(i,:)=[X_mm Y_mm Z_mm];
end
IK_pro600(coords,startpos)
    % server_ip = '192.168.1.159';
    % server_port = 5001;
    % robot = importrobot('URDF/pro600.urdf');
    % robot.DataFormat = 'row';
    % show(robot);
    % ik = inverseKinematics("RigidBodyTree",robot);
    % weights=[1,1,1,1,1,1];
    % 
    % % show(robot,configSol)
    % % view(90,80)
    % for i=1:length(coords)
    %     aimPose=trvec2tform(coords(i,:))* eul2tform([0, -pi/2, 0]);
    %     [configSol,solInfo] = ik('link6',aimPose,weights,startpos);
    %     startpos=configSol;
    %     targetSol1=rad2deg(configSol);
    %     targetStr1 = sprintf('set_angles(%.4f, %.4f, %.4f, %.4f, %.4f, %.4f, 500)',targetSol1(1),targetSol1(2),targetSol1(3),targetSol1(4),targetSol1(5),targetSol1(6));
    %     % disp(targetStr1)
    %     send_tcp_packet(server_ip,server_port,targetStr1);
    %     show(robot,configSol)
    %     view(-90,70)
    %     pause(0.1)
    % end


















% if data(1,1)==data(2,1)
%     first_cord=1;
%     second_cord=0;
% else
%     first_cord=0;
%     second_cord=1;
% end
% coords=[data(1,:)];
% for i=1:data_len-1
%     if data(i,1)~=data(i+1,1) && first_cord==1
%         coords=[coords; data(i,:)];
%         first_cord=0;
%         second_cord=1;
%     end
%     if data(i,2)~=data(i+1,2) && second_cord==1
%         coords=[coords; data(i,:)];
%         first_cord=1;
%         second_cord=0;
%     end
% end
% coords=[coords;data(data_len,:)];
% waypoint_generation(coords)
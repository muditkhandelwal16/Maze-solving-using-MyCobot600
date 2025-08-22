function iksoln=IK_pro600(pose,startpos)
    server_ip = '192.168.1.159';
    server_port = 5001;
    robot = importrobot('URDF/pro600.urdf');
    robot.DataFormat = 'row';
    show(robot);
    ik = inverseKinematics("RigidBodyTree",robot);
    weights=[1,1,1,1,1,1];
    
    % show(robot,configSol)
    % view(90,80)
    for i=1:length(pose)
        aimPose=trvec2tform(pose(i,:))* eul2tform([0, -pi/2, 0]);
        [configSol,solInfo] = ik('link6',aimPose,weights,startpos);
        startpos=configSol;
        targetSol1=rad2deg(configSol);
        targetStr1 = sprintf('set_angles(%.4f, %.4f, %.4f, %.4f, %.4f, %.4f, 500)',targetSol1(1),targetSol1(2),targetSol1(3),targetSol1(4),targetSol1(5),targetSol1(6));
        % disp(targetStr1)
        send_tcp_packet(server_ip,server_port,targetStr1);
        show(robot,configSol)
        view(-90,70)
        pause(0.1)
    end
end
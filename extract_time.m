%%%%%%%%%% Combined script of cropping, mover create and image sequence from
%%%%%%%%%% video
%%%%%%%%%%Instruction:
%%%%%%%%%% - edit bar_dist and TUI_dist if needed
%%%%%%%%%% - edit the value of video_dir to the folder where the videos are found
%%%%%%%%%% - the first window will appear to ask for two points to measure
%%%%%%%%%% distance
%%%%%%%%%% - click on two points along the distance measurement bars to signifies
%%%%%%%%%% the distance of 10mm
%%%%%%%%%% - A new window appear that calls the user to create the cropping
%%%%%%%%%% box
%%%%%%%%%% - draw a bounding box and adjust to include the object of
%%%%%%%%%% interest
%%%%%%%%%% - right click within the box and click "crop image"

bar_dist=10; % gauge bar distance of the two points, chosen to be 10mm
TUI_dist=0.5; % please change the TUI dist %distance of vertical slice
max_time=1;
largest_time=1; %time at diastole
video_dir='C:\Users\maria\OneDrive\Documentos\Coding\Year4Project\Tools_Data\original_images\Healthy\21.57wks_13Apr2021P2\13APR2021P2_1';

Obj=VideoReader([video_dir '\video\' sprintf('time%d.avi',largest_time)]);
vid=read(Obj);
numFrame = get(Obj, 'numberofFrame');

start_end=[];
i=1;
while 1
    imshow(vid(:,:,:,i));
    T=waitforbuttonpress;
    T=double(get(gcf,'currentcharacter'));
    if T==28 %left arrow
        i=i-1;
        if i<1
            i=1;
        end
    elseif T==29
            i=i+1;
            if i> numFrame
                i=numFrame;
            end
    elseif T==13
        start_end=[start_end i];
        if length(start_end)==2
           break; 
        end
    end
end
hold off;
close all
    
img=(vid(:,:,:,floor(size(vid,4)/2)));
figure('Name','choose two points to measure distance');
imshow(img); %%show image
hold on;
dist = ginput(2);
close all;
num_pix= abs(dist(1,2)-dist(2,2));
pixres= bar_dist/num_pix;
B = cd (video_dir);
fileID = fopen('scale.txt','w');
fprintf(fileID,'%f ',[pixres,pixres,TUI_dist]);
fclose(fileID);
figure ('Name','crop, create the box, right click on the box and choose "crop image"');
[cropped rect]=imcrop(img);
close all;

for i=1:max_time
Obj=VideoReader([video_dir '\video\' sprintf('time%d.avi',i)]);
vid=read(Obj);
B = cd ([video_dir]);
%B = cd ('../');
mkdir(['time' sprintf('%3.3d',i)]);
B = cd (['time' sprintf('%3.3d',i)]);
for count = start_end(1):start_end(2)
    img = vid(:,:,:,count);
    if (~isempty(rect))
       cropped= imcrop(img,rect);
       else display('error');
    end
    cropped=rgb2gray(cropped);
    imwrite(cropped,['slice' sprintf('%3.3d',count-start_end(1)+1) 'time' sprintf('%3.3d.png',i)],'png');
end
end

%%

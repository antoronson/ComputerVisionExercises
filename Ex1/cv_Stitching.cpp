#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;

int main(){
    // Read Image file and display

    std::string image_path = "1.jpg";
    Mat ipImage = imread(image_path, IMREAD_COLOR);

    imshow("Test Image", ipImage);

    int k = waitKey(0);

    return 0;

}
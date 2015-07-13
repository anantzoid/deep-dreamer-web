#Deep Dreamer
Web client for Google's [deepdream]

The original implementation has been provided by google [here]. You can find the installation instructions for all the prequisite requirements over there. For more info and tips, you can refer to [this] reddit post.

### Installation Information
The deepdream generator is based on a cron right now, so make an entry in the crontab for every minute.

>Note that this project is still under development and the following features are left to be implemented:
  - Addition of [CuDNN] to make the computations faster
  - Relative compression depending on file size
  - Gallery
  - Option to mail the generated image
  - Generate more variations of deepdream
  

[here]: https://github.com/anantzoid/deepdream
[deepdream]: http://googleresearch.blogspot.co.uk/2015/06/inceptionism-going-deeper-into-neural.html
[this]:https://www.reddit.com/r/deepdream/comments/3cawxb/what_are_deepdream_images_how_do_i_make_my_own/
[cuDNN]: https://developer.nvidia.com/cudnn


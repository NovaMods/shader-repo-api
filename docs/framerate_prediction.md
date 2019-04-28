# Framerate Prediction

Nova will collect framerate data from people who have opted in. The data will include hardware information, what shader
options are enabled, maybe some information about the world, and the user's framerate. All this data will be uploaded to
a database in the Shader Repo

## Statistics

The performance data will be aggregated and displayed on the shader's page. The Shader Repo will calculate the average
framerate of a shader on a variety of GPUs and will display a matrix of GPU and shader options profile

Example performance matrix:

| GPU      | Low | Medium | High |
|----------|-----|--------|------|
| GTX 660  |  30 |     25 |   15 |
| GTX 780  |  50 |     35 |   20 |
| RTX 2080 |  60 |     60 |   60 |

Shader devs will have much more granular information. They'll be able to see both the actual performance of their shader 
with a specific set of options on specific hardware, and the frametime cost of each option

## Machine Learning

The Shader Repo will run the performance data through a machine learning algorithm, probably a decision tree. The
machine learning will learn how to predict framerate given hardware and shader information. This will help to fill in
the performance matrix for hardware that the shader hasn't been run on yet, and will allow users to input their
hardware and see how they expect the shader to perform on their system. This will only be enabled for shaderpacks that
are popular enough to have enough data to meaningfully train the decision tree

The raw data uploaded will almost certainly have a lot of duplicate entries, since people tend to not change shader
options very much during normal gameplay. Removing those duplicates will be very important to ensure the decision trees
don't overfit the data

## Manual Data Collection

While collecting data from normal gameplay will be very accurate, it won't necessarily be very complete, especially for
less popular shaders. Thus, we'll develop a tool in Nova that can collect performance information on a target scene. The
tool will try all shader options, enabling them all individually and together to try and get a good idea of the shader's
performance. This tool will be available to the general public, and will likely be suggested on the pages of less popular
shaders

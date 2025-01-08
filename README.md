# DroneUAV UDP Video Decoder

## Overview

This code is developed specifically for decoding certain UDP video streams from drone (UAV) communication packets. The class processes JSON files containing raw packet data, extracts the video payloads, and collates them into a sequence of images. These images are then converted into a playable video format or streamed in real-time.

## Features
- First extract and collate the relevant UDP video stream payload data. This code works with the export saved as a json from Wireshark
- Partitions the UDP data stream in image data and reconstructs that data as a JPEG frame for each
- Collates the JPEG frames and saves them as videos
- Saves the image sequence as a video file.



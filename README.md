# Chess-Playing-Robot
A camera-equipped robotic arm that can play chess against a human through gripping and moving the chess pieces.
## How it works
### Step 1: Getting the opponent's move
We first need to get the move played by the opponent from a perpendicular image to the chess board. Since we know the starting position of each chess piece, we only need to keep track of the changes. By comparing the old and the new chessboards, we can get the move by finding a chess square that was free and got occupied. We can then get the type of the chess piece by finding the square which was occupied and became free.
<p>
We perform computer vision in two ways:
  * Chessboard segmentation: We divide the chessboard into 64 square
  * Color segmentation: For each chess square, we detect whether it is free or occupied with either piece of ours or the opponent's
</p>
### Step 2: Calculating the right move
By supplying the last move to the open-source stockfish chess engine, along with other arguments, we can compute the correct move.
### Step 3: moving the piece
Since the robotic arm can reach any square on the chess board by rotating the stepper motors to reach fixed angles relative to the home position, we map the original and destination chess squares to their corresponding angles. The robotic arm can then move from the home to the source chess square, grab the piece, go to the home position, and then finally drop the chess piece into the destination square.

## Resources
* https://howtomechatronics.com/projects/scara-robot-how-to-build-your-own-arduino-based-robot/
* https://pypi.org/project/stockfish/
* http://www.raspberryturk.com/

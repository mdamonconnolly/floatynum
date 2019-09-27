

//Prints it out as a graph.
fn update_display(byte_stream:&[i16;64])
{
    for i in (0..13).rev() {
        for j in 0..63 {
            if byte_stream[j] == i {
                print!(" {0} ", byte_stream[j]);
            }
            else {
                print!(" · ");
            }
        }
        print!("\n");
    }
}

/*
fn compressor_node(threshold:i16, ratio:i16, mut &_byte_stream:[i16;64])
{
    for i in 0..63
    {
        _byte_stream[i] = ((_byte_stream[i] - threshold) / ratio) + threshold;
    }
}
*/

fn blip(position:usize, magnitude:i16, Q:i16, mut byte_stream:&mut [i16;64])
{
    byte_stream[position] = magnitude;
    calculate_falloff(position, Q, byte_stream);

    //Calculate Falloff
}

//Main function with array stream.
fn main() {
    
    //Test cases can change here.
    let mut stream:[i16;64] = [0;64];

    blip(22, 5, 3, &mut stream);

    update_display(&stream);
}

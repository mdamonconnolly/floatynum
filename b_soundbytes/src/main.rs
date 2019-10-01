

//Prints it out as a graph.
fn update_display(byte_stream:&[i8;64])
{
    for i in (0..10).rev() {
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

//Main function with array stream.
fn main() {
    
    //Test cases can change here.
    let mut stream:[i8;64] = [0;64];

    blip(16, 4, &mut stream);
    blip(38, 8, &mut stream);

    update_display(&stream);
}



//Prints it out as a graph.
fn update_display(_byte_stream:[i16;64])
{
    for i in (0..10).rev() {
        for j in 0..63 {
            if _byte_stream[j] == i {
                print!(" {0} ", _byte_stream[j]);
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
    let mut stream:[i16;64] = [0;64];


    update_display(stream);
}

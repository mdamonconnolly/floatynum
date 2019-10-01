use std::time::SystemTime;
use std::time::Duration;

//TODO: Will this work with new update.
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

    let mut tick = SystemTime::now();

    loop{  

        let deltaTime = Duration::from_millis(1000);

        if deltaTime.as_secs() >= tick
        {
            println!("LALALALA");
        }

        println!("{:?}", deltaTime.as_secs());
        
    }

    update_display(&stream);
}

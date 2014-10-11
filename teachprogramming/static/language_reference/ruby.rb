# Ruby            # VER: title


def hello_world()
    puts "Hello World"        # VER: hello_world
end


def read_line_from_console()
    def gets()
        return 'bob'
    end
    username = gets            # VER: read_line_from_console
    puts(username)
end


def comment()
    #This is a comment  # VER: comment
end


def file_read()
    line_count = 0                              # VER: file_read
    File.open("in.txt", "r") do |infile|        # VER: file_read
        while (line = infile.gets)              # VER: file_read
            puts "Line #{line_count}: #{line}"  # VER: file_read
            line_count = line_count + 1         # VER: file_read
        end                                     # VER: file_read
    end                                         # VER: file_read
end


def define_variables()
    count = 0            # VER: define_variables
    username = "Betty"   # VER: define_variables
    distance = 3.14      # VER: define_variables
    email_errors = True  # VER: define_variables
end


def define_constats()
    #GRAVITY = 9.81  # VER: define_constants
end


def arithmetic()
    xpos = 0
    item_price = 0
    quant = 0
    count = 0
    
    xpos = xpos + 1                  # VER: arithmetic
    distance = 3 / 4                 # VER: arithmetic
    total_cost = item_price * quant  # VER: arithmetic
    remainder = 14 % 11              # VER: arithmetic
    count += 1                       # VER: arithmetic
end


def if_statement()
    username = 'bob'
    count = 3

    if count >= 5 and username == "Jim"  # VER: if_statement
        puts("Yes")                      # VER: if_statement
    elsif username == "admin"            # VER: if_statement
        puts("Admin")                    # VER: if_statement
    else                                 # VER: if_statement
        puts("No")                       # VER: if_statement
    end
end

read_line_from_console()
file_read()
if_statement()
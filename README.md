![Platform: ALL](https://img.shields.io/badge/platform-ALL-green)
![Dependencies: python3+](https://img.shields.io/badge/dependencies-python3+-blue)
![Version: 1.5.0](https://img.shields.io/badge/version-1.6.2-green)
![Follow @rubynorails on Twitter](https://img.shields.io/twitter/follow/rubynorails?label=follow&style=social)

# brutalist
`brutalist` is a python3-based command-line tool for all platforms that can be used to generate quick and large word lists from one or more sample passwords provided by the user.

### Use case:
Let's say you come across an outdated password in an old credential dump, but the user has since updated their password (`password`) to `P@$$w0rd123!`.
If fed the word `password`, `brutalist` can generate up to 6,013,440 unique custom combinations of that specific word.
It can use various methods of leet speak substitution, as well as other common special character substitutions, suffixes, and special character additions -- all while keeping the order of the original characters in the password.

### Notes:
Running without the `--limit-special`, `--limit-numbers`, or `--limit` options, the number of results is exponentially increased and may take some time to generate the list.

Running with the `--leet` option will exponentially increase the results, and I have no idea how long it will take, because I have never sat around to wait on it to finish.

## Install via Git:
1. `git clone https://github.com/phx/brutalist.git`
2. `cd brutalist`
3. `sudo cp brutalist.py /usr/local/bin/brutalist`

You can just as easily execute it where it stands or manually copy it elsewhere in your `$PATH`.

## Install via Homebrew on MacOS:
1. `brew tap phx/brutalist`
2. `brew install brutalist`

## Run:
```
Usage: brutalist <[password] | -p [password] | -i [input file]> <[extended options]>

Options:
       [no params]                             takes input from stdin.
       [string]                                first argument is used as password.
       -p | --password                         second argument is used as password.
       -i | -f | --file [input file]           file is used as input.

Extended Options:
       -c | --limit-special | --limit-chars    limits special characters to '!@#$%*-+_'
       -n | --limit-numbers                    only includes common 1 and 2 digit suffixes + special
       -l | --limit                            limits both 3 digit numbers and special characters
            --leet                             includes all leet speak combinations (will increase size and time)
```
## Examples
- From the downloaded git repo working directory:
 `./brutalist.py [a single password]`
- Installed via `homebrew` or copied to your `$PATH` as `brutalist`:
` brutalist [a single password]`
 
Going forward, we will reference the command as `brutalist` -- just know that if it's not in your `$PATH`, it will have to be run in-place as `./brutalist.py`.

- `stdin`from pipe, `stdout` to a file:
`cat small_list.txt | brutalist > huge_list.txt`
- `stdin` from input redirection, `stdout` to a file:
`brutalist < small_list.txt > huge_list.txt`
- input file as argument, write to both file and `stdout`:
`brutalist -i /path/to/small_list.txt | tee huge_list.txt`
- `stdin` from user input (outputs to `stdout`):
`brutalist`[type your sample password(s), then hit `Ctrl-D`]


### Background
This program is by no means perfect.  It's quick and dirty, and by no means optimized.  I started out in C before realizing that Python would do a much better job, and it's still extremely fast when it comes to generating these word lists.  Almost instant.

I wrote this over the course of a few hours because it was something I had been thinking about that solved a particular use-case I had come across on multiple occasions, and while BurpSuite Pro offers some similar functionality, you have to fool around with it every time to get something close to what you want, as opposed to just running a simple command using `brutalist` . 

### To-Do, Updates, and Contribution
I plan to add the option to specify the special characters used in the suffix, which can greatly cut down on the number of permutations for those who need shorter lists.  There will be some permutations that are missing, which I may add code for at a later point.  If you want to contribute or clean up the code, feel free to submit a pull request.

### Disclaimer
By downloading and running this software, you agree to only use it for ethical purposes and also agree to be held fully liable and accountable for any damage or harm caused by using `brutalist`.

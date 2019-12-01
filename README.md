![Platform: ALL](https://img.shields.io/badge/platform-ALL-green)
![Dependencies: python3+](https://img.shields.io/badge/dependencies-python3+-blue)
![Version: 1.7.0](https://img.shields.io/badge/version-1.7.0-green)
![Follow @rubynorails on Twitter](https://img.shields.io/twitter/follow/rubynorails?label=follow&style=social)


![brutalist](./brutalist.png?raw=true)

# brutalist
`brutalist` is a python3-based command line tool for all platforms that can be used to generate quick and large word lists from one or more sample passwords provided by the user.

### Use case:
Let's say you come across an outdated password in an old credential dump, but the user has since updated their password (`password`) to `P@$$w0rd123!`.
If fed the word `password`, `brutalist` can generate up to a few million unique custom combinations for that specific word.
`brutalist` uses various methods of leet speak substitution, as well as other common special character substitutions, suffixes, and special character additions -- all while keeping the order of the original characters in the password.

### Notes:
Running without the `--limit-special`, `--limit-numbers`, or `--limit` options decreases the number of results to something manageable.

Running with the `--leet` option increases the number of results exponentially to something quite large.

The time it takes to return the results depends on the initial password length.

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
            --leet                             includes all leet speak combinations (will increase size)
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
`brutalist -f /path/to/small_list.txt | tee huge_list.txt`

### Runtime samples for using the password example "password":
```
---------------------------------------------------------
$ time echo password | brutalist
...
real    0m30.776s
user    0m23.589s
sys     0m4.892s
...
$ echo password | brutalist | wc -l
 7643680
---------------------------------------------------------
$ time echo password | brutalist --leet
...
real    1m1.169s
user    0m41.930s
sys     0m9.094s
...
$ echo password | brutalist | wc -l
 13198680
---------------------------------------------------------
$ time echo password | brutalist --limit-special
...
real    0m16.423s
user    0m11.681s
sys     0m2.582s
...
$ echo password | brutalist --limit-special | wc -l
 3821840
---------------------------------------------------------
$ time echo password | brutalist --limit-numbers
...
real    0m0.633s
user    0m0.439s
sys     0m0.109s
...
$ echo password | brutalist --limit-numbers | wc -l
  134160
---------------------------------------------------------
$ time echo password | brutalist --limit
...
real    0m0.352s
user    0m0.234s
sys     0m0.059s
...
$ echo password | brutalist --limit | wc -l
   68800
---------------------------------------------------------
```
### 10 random samples from password example "boot":
```
$ time echo boot | ./brutalist.py --leet | sort -R | head -10
13oOT225)
3oO7721)
BOO7791.
130Ot814%
b0O+538.
B0OT059&
13Oot786=
3OOt899)
3OO+631!
B0O+313]

real    1m40.766s
user    1m41.305s
sys    0m0.491s
```

### Background
I started out in C before realizing that Python would do a much better job, and it's still pretty fast when it comes to generating these word lists.

I wrote this over the course of a few hours because it was something I had been thinking about that solved a particular use-case I had come across on multiple occasions, and while BurpSuite Pro offers some similar functionality, you have to fool around with it every time to get something close to what you want, as opposed to just running a simple command using `brutalist` . 

### Contribution
If you want to contribute or help clean up and optimize some code, feel free to submit a pull request.

### Disclaimer
By downloading and running this software, you agree to only use it for ethical purposes and also agree to be held fully liable and accountable for any damage or harm caused by using `brutalist`.

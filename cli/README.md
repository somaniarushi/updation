# Command Line Tutorial

## Command Line Basics
1. Arguments: Required parameter. Example: `pip install django`
2. Options: Unrequired parameter. Example: `pip install django --cache-dir ./dir`
3. Flag: Enable or disable a certain feature. Example: `pip install django --verbose`

## Different Technologies Used
1. Argparse: Works, but is faily complicated and not very scalable.
2. Click: Good for simple, non-interactive CLIs.
3. PyInquirer: Necessary for interactive CLIs that are dynamic and easier to use.

---
Release Puller
---

## Summary

Release Puller is a python tool devloped by Sam Handler for getting product sources from Release\_Tree for building a functioning environment.  Release Puller can use a variety of sources to create a list of products and versions.

## Configuration

There is a file inside of the releasepuller root directory called ReleasePuller.rc which 


## Usage

**note:** All the commands given can be abreviated to the letters which uniquely determines them.  For instance `add versionsource compilerequest` can be shortened to `a v co`.  We need to specify `co` instead of just `c` since `a v c` could mean `add versionsource compilerequese` or `add versionsource csuites`.



### add

#### add all

Adds all products known in the version source. Not recommended.

#### add cvs

Adds a CVS selection to the release items.

#### add group

Adds all products in the specified group to the build

#### add product

Adds a single product to the build.

#### add versionsource

##### add versionsource brick

Adds a version source that uses the Brick/Build schedule.

##### add versionsource compilerequest

Adds a version source that uses a compile request.

##### add versionsource csuites

Adds version source for each suite from the compile request.

##### add versionsource series

Adds a version source that uses a monarch series.

##### add versionsource suite

Adds a version source that uses a product suite.

#### add zipfile

Adds a zip file to the release items.

### build

Coppies listed files from release tree, unzips into specified directory and compiles using *Compile N Build*.


### compile

Runs the compile script.
Requires the monarch\_script configvar to be set, if unified mode is off and building the monarch directory.
Requires the monarchnet\_script configvar to be set if unified mode is off and building the monarchnet directory.
Requires the unified\_script configvar to be set if unified mode is on.

### createProductText

Creates a file in name listing all of the paths to specifiedproducts.  This is necessary before building, pulling, etc...

### exit

Exit program.

### help

Displays help information for full command.

### list

#### list configvars

Lists the configvars currently included in the build.

#### list groups

Lists the groups

#### list name

Lists the build name.

#### list path

Lists the build path.

#### list releases

##### list releases monarchType

Lists the release items currently included in the build, sorted by monarchType??

##### list releases name

Lists the release items currently included in the build, sorted by name.

##### list releases order

Lists the release items currently included in the build, sorted by order added.


#### list unified

Lists the unified flag.

#### list versionsources

Lists the currently selected version source(s)

### pull

#### pull files

Puts the files for the release into the correct directories. Does not compile.

#### pull zipfiles

Puts zip files for the release items into the correct directories.


### remove

#### remove all

Removes all release items.

#### remove group

Removes all products in the specified group from the build.

#### remove monarch

Removes all monarch-side release items.

#### remove net

Removes all monarchNET-side release items.

#### remove product

Removes all releases with the corresponding product name from the build.

#### remove release

Remove a specific release item.

#### remove versionsource

Remove a specific version source.

### save rels

Save to the specified file a list of commands that can be used to re-add the currently added releases.
If no file is specifed, print the output to the terminal.

### set

#### set configvar

Sets a configuration variable. These are installation-specific settings.

#### set group

Defines a group.

#### set name

Sets the name of the build.

#### set path

Sets the path of the build.

#### set releasesource releasetree

Sets the release source to be the Release Tree.
Before calling this command, it is recommended that the configvars release_tree_path and platform_string be set.
See the documentation for 'set configvar'.

#### set unified

Sets whether to unify the monarch/MonarchNET trees.

### source

Read lines from a file and execute them as commands. Lines starting with "#" are ignored.

### threadTrain



### version

Prints version information.






## Compile N Build

Compile N Build is a tool developed by Jeremy Mattke to build an environment after releases have been pulled by release puller.  The functionality of Compile N Build .

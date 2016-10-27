---
title: Setting Up an Environment
---

# Setting Up an Environment

## Preparation

1.  Choose a directory where the new environment will go.  Many developers will create a folder `D:\osi` for all their environments.  They will then create a folder inside of `D:\osi` for their new environment.  This folder name is of your choosing (it can be something like *PAC* or *EVN* if building a system similar to customer system or something like *40_2_1* or *44\_1\_1* if it is a particular monarch version or *11\_1\_1* to match the Platform Suite).  We will refer to this environment folder as `$OSI`.

2.  Create the following three directories

	```language-batch
	$OSI\monarch
	$OSI\osi_cust
	$OSI\products
	```

3.  Make sure the correct version of *Visual Studio* is in your path.

	For 32 bit compiles use Visual Studio 8:

	```language-batch
	SET PATH=C:\Program Files (x86)\Microsoft Visual Studio 8\VC\bin;C:\Program Files (x86)\Microsoft Visual Studio 8\VC;%PATH%
	```

	for 64 bit compiles use Visual Studio 10

	```language-batch
	SET PATH=C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin;%PATH%
	```

	**note:** Visual Studio is used form compilation.


## Getting Releases

1.  Use "Release Tools" (Tim McDougall's tool) or [Release Puller](/EMS/EMS_release_puller.html) (Sam Handler's tool) to get releases for the desired monarch version, suite versions, or compile request (you need to tell release puller the version source of the compile request, then add the files you want, like add all, then pull the files).

2.  Unzip releases to `$OSI/monarch` directory (also unzip ant and jdk from release tree)

		monarchNET->BaseNET->osii_ant
		monarchNET->BaseNET->osii_jdk

	and put in common location such as 

		D:\ant
		D:\jdk

	Since these are rather large and do not change from release to release we can just unzip one and use it for all monarch environements.

3.  Copy profile `monarch_xp_x64.bat` (or `monarch_xp.bat` for 32 bit compiles) script from `$OSI/monarch/scripts` to `$OSI/monarch`.

4.  Update `ANT_HOME` and `OSI_JDK_HOME` environment variables in `monarch_xp_x64.bat` to point to the common directories assigned in step 2.


5.  Modify `monarch_xp_x64.bat` starting with `rem Set OSI path reference variables` to read the following:

	```language-batch
	rem Set up OSI path reference variables
	SET OSIINET=<$OSI>\monarch
	SET OSI=<$OSI>\monarch
	SET JOB=<$OSI>\osi_cust
	```

	where `<$OSI>` is the path to the environment folder created above.

	**note:** You may need to change vcvarsall to target the batch file for visual studios.

	**note:** If you are doing a 32 bit compile you will use `monarch_xp.bat` instead of `monarch_xp_x64.bat`.


## Compiling Environment

1.  Run the profile script to setup environment variables.

	```language-batch
	monarch_xp_x64.bat
	```

2.  From `$OSI` run the setup script to set some additional variables for compilation.

	```language-batch
	scripts/setup
	```

3.  Compile base and basenet

	```language-batch
	cd $OSI/monarch/src/base_net
	make
	cd $OSI/monarch/src/base
	make
	```

4.  To setup licensing

	```language-batch
	cd $OSI/monarch/src/base/util/license/setlicense
	make
	cd $OSI/monarch
	osi_setlicense -easy
	```

	**note:** this gives a 30 day license after which point it will need to be renewed.

5. Schema all the databases (this creates header files for many products and db files.)

	```language-batch
	cd $OSI
	schema_all
	```

	**note:**, after compilation the `schema_all` command will erase any data stored in the db files.

6. From `$OSI` Populate the base database files (TODO: update explaination)

	```language-batch
	pop_base
	DBMS_config_set_for_net
	```

7. Compile remaining products

	```language-batch
	cd $OSI/monarch/src
	make
	```

	**optional:** Remove `make.bat` from `$OSI/src` to prevent accidentally doing `make clean` later.

8. Create `osiprojectedit`

	```language-batch
	cd $OSI/monarch/srcNET/BaseNET
	make
	```

	**note:** `osiprojectedit is a utility which converts all C# files in a directory (recursively) to OSI format. We use it in these directions to convert C# files to 64 bit.

9. If doing a 64 bit build, convert 64 bit C# files to 64 bit.

	```language-batch
	osiprojectedit -t x64
	```

10. Build srcNET C# projects

	```language-batch
	cd $OSI/monarch/srcNET
	make
	```

11. Build Java projects

	```language-batch
	cd $OSI/monarch/srcJava
	make
	```

12. I don't know what this does:

	```language-batch
	objserver
	```

13. Generate `osii_agent.xml` in `$OSI/monarch/profiles`

	```language-batch
	osii_agent
	```

	After `osii_agent` has started successfully, find the process in the task manager and kill it.

	Alternatively `osii_agent.xml` can be coppied from another build.

15. Modify `osii_agent.xml` so that localhost is your `<localhost>` (hostname of your machine)

	**optional:** Modify `osii_agent.xml` replacing SAMPLE with the environment name (like `40_2_1` or `43_2_2`. This will be the `<domain name>`). If you skip this step, SAMPLE will be your `<domain name>`, which is fine.

16. Modify `net_autostart.bat` in `$OSI/monarch/scripts` to start domain `<domain name>` and to run faster by removing `which` check

17. I am not sure what this does

	```language-batch
	passwdutil disable
	```

18. Modify `security.rc` in `$OSI/monarch/sys/rc` change one of the allow rows from `dac1 full` to `DefaultConsole full` (move to job folder)

19. I am not sure what this does 

	```language-batch
	osii_uds_import --domain <domain name> --new
	```

20. Start MonarchNet processes:

	```language-batch
	net_autostart
	```

21. Import states tables information

	```language-batch
	osii_states_converter --domain <domain name>
	```

22. I am not sure what this does

	```language-batch
	DisplayConverter --domain <domain name> -user admin -pwd admin -c -d -u
	```

23. Update `osii_rdbms_adaptor.jrc` file in `$OSI\profiles\<domain name>\config`

	**note:** Any processes connecting to messaging must be an authorized process, the list of which can be edited in `monarch\profiles\<env name>\config\osii_mcp.xml`



## Starting an Environment

1.  Make sure the correct version of *Visual Studio* is in your path.

	For 32 bit use Visual Studio 8:

	```language-batch
	SET PATH=C:\Program Files (x86)\Microsoft Visual Studio 8\VC\bin;C:\Program Files (x86)\Microsoft Visual Studio 8\VC;%PATH%
	```

	for 64 bit use Visual Studio 10

	```language-batch
	SET PATH=C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin;%PATH%
	```

	**note:** Visual Studio is used form compilation.

2.  From `$OSI` run the monarch profile script

	```language-batch
	cd $OSI
	monarch_xp_x64.bat DEBUG
	```

	**note:** the DEBUG option is so any compiles that are doen will be done with debug information, allowing debugging in Visual Studio.

3.  From `$OSI` start MonarchNet Services:

	```language-batch
	scripts\net_autostart 
	```


3.  Start OpenViewNet

	```language-batch
	openviewnet -d
	```

	**note:** the `-d` switch creates a debug window to go along with OpenViewNet which is very handy.


## Killing an environment

1. Run the following:

	```language-batch
	osii_shutdown
	osi_shutdown
	```

2. Verify in Task Manager that no osi processes are running.


## Building on Windows

## Building on Linux

## Building on AIX


1. On a windows/linux machine open up `ReleasePuller.rc`

2. update the platform to be `aix`.  If using the AIX development box, make sure that the archetecture is set to 64bit

3. Set name and pull files

4. Make sure that OSI toolkit and OSI toolkit-secure sockets are included.

5. zip up files and send to AIX box.

6. unzip files where you want your environment.  Make sure to use the `-a` option so that end of line characters are converted if necessary.

7. Set the following two variables:

	```language-bash
	export PATH=$PATH:/usr/var/bin:/usr/vacpp/bin
	export CXX=/usr/vacpp/vin/xlC
	```


8. verify that scripts are executable





9. run the profile script

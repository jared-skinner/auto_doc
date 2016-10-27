---
title: OpenNet Release Checklist
---


## OpenNet Release Checklist


### Creating the Beta

[] Verify that all SWR branches have been merged to the development branch.

	The following jira query can be used to check:

	project = "Software Work Request" AND Product = OpenNet AND "Target Product Release" ~ <product release> AND status != "Ready For Test"


[] Check that the rel branch and rel tag are filled in for each ticket.


[] Review any schema changes. See if these changes affect one of the several objects that have field-for-field duplicates elsewhere in the schema; update these copies if necessary.

	The schema file should have notes at the beginning of each object stating things which should be the same between objects.


[] If the release contains schema changes, notify the OTS Team.


[] Copy OPENNET.SKM to OPENNET2.SKM


[] **5.99.x and later** Copy OPENNET.SKM to OPENNET_CA_BASE.SKM).


[] Copy OPENNET.SKM to compare/OPENNET.SKM - add compare flags to all fields.

	Use the script create_compare_schema.py and provide the path to the OPENNET.SKM file.  It will generate a file called OPENNET_COMPARE.SKM.  Winmerge this generated file with the file in OpenNet_compare


[] If database objects have been added or changed names, update the database XML files appropriately.


[] **6.1x and later** If database input fields have been added, update src_model_table in opennet_database_info.h.

	opennet_database_info.h is in src/opennet/include. Input field should be given an e flag or an r flag.  Make sure to update SRC_MODEL_TABLE_SIZE to account for updates to the size of src_model_table.


[] If files have been added/removed, make sure the .rel and .reslist files have been appropriately updated and that the eol-style and mime-type are correct for the new file(s).


[] **5.5.x and later** Run the check_tabulars.py and scan_message_strings.py scripts (both in the OpenNet repo under script/opennet).  These should not return any errors.

	If errors appear, run the script on the old vs new release and look for differences.


[] **6.2.x and later** Run the check_schema.py script (in SVN).


[] **5.5.x and later** If new displays have been added, update the drop-down button on all Default [\*] Panel.atds


[] Update rel file with version number (e.g., onet_v6.4.0.0_beta01_bin/src).


[] Make commit & tag with beta version tag (v6_4_0_0_beta01).


[] Copy the tag path to the Source tab of the Release Management Tool (e.g., tags/v6_4_0_0_beta01, and run Generate Source Release.


[] Announce the existence of a beta version of the software to the `EMSTEAM` email alias.


### Testing


[] Ensure that WRs have the impact and release notes properly filled out in JIRA.


[] Fill out release information in Release Management Tool - note added/removed binaries in the Developer Notes.

	When filling out the release information use a previous release as a model.  

	Any new executables should be listed in the comments->developer notes and deployment->green plus sign.  Fill out the process name and give a description of what the process does.


[] Perform functional testing.


[] Move any changes from testing back to the development branch. Be careful about display changes, as they will not show up in a standard diff unless the files are moved to the "FACTORY_DEFAULT/tabulars" folder.


[] Merge any testing changes back to the original development branches, if possible; update tags in JIRA.


### Releasing

[] If the release contains schema changes, check to see if OPENNET.DAT and OPENNET2.DAT need to be updated.


[] Update version information (include/opennet_version.h).


[] Update schema files with version number.

	The version is found at the beginning of the schema file.


[] Update opennet.rel and opennet_unit_test.rel with version number (e.g. onet_v6.4.0.0_bin/src)


[] **6.1x and later** Update opennet_intutil.rel with version number.


[] Make commit & tag with version tag (v6_4_0_0).


[] Copy the tag path to the Source tab of the Release Management Tool (e.g., tags/v6_4_0_0), and run Generate Source Release.


[] If documentation updates are needed, create the appropriate SWRs and links to originals.


[] If upmerges/backmerges are needed, create the appropriate SWRs and links to originals.


[] Request release approval via Release Management tool.


[] Once the release has been approved, announce the release via Release Management tool.


[] Review the release status of previous releases; update these as needed.

	This really only needs to be done if I am issuing a patch for a broken release.

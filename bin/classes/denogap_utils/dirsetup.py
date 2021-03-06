#!/usr/bin/env python
import os
import sys
from collections import defaultdict

class SetDir:
	"""
	This class is for setting-up output dirs for DeNoGAP
	"""
	
	def __init__(self):
		self.iterdir_dict=defaultdict()
		self.projectdir_dict=defaultdict()
		
	def mk_project_dirs(self,project_dir):
		"""
		This function creates nested sub-directories 
		under specific project path
		"""
		
		### If not already present create sub-directories for DENOGAP HMM ####		
		if not os.path.exists(os.path.join(project_dir,"DENOGAP_HMM")):
			os.makedirs(os.path.join(project_dir,"DENOGAP_HMM"))
		self.projectdir_dict["BASE"]=os.path.join(project_dir,"DENOGAP_HMM")
		
		if not os.path.exists(os.path.join(project_dir,"TMP")):
			os.makedirs(os.path.join(project_dir,"TMP"))
		self.projectdir_dict["TMP"]=os.path.join(project_dir,"TMP")
		
		if not os.path.exists(os.path.join(project_dir,"HMMER_DB")):
			os.makedirs(os.path.join(project_dir,"HMMER_DB"))
		self.projectdir_dict["HMMER_DB"]=os.path.join(project_dir,"HMMER_DB")
			
		if not os.path.exists(os.path.join(project_dir,"HMMER_DB","SEQ_DB")):
			os.makedirs(os.path.join(project_dir,"HMMER_DB","SEQ_DB"))
		self.projectdir_dict["SEQ_DB"]=os.path.join(project_dir,"HMMER_DB","SEQ_DB")
		
		if not os.path.exists(os.path.join(project_dir,"HMMER_DB","HMM_DB")):
			os.makedirs(os.path.join(project_dir,"HMMER_DB","HMM_DB"))
		self.projectdir_dict["HMM_DB"]=os.path.join(project_dir,"HMMER_DB","HMM_DB")
		
		
		return(self.projectdir_dict)
		
		
	### Function to setup project dir ####	
	def mk_hmm_iter_dirs(self,project_dir,iter_num):
		"""
		This function creates project directory if not exist.
		It also create missing sub-directories for storing DeNoGAP-HMM output
		Input: project dir path
		"""
		iter_dir="iter_{0}".format(iter_num)
		
		
		if not os.path.exists(os.path.join(project_dir,"DENOGAP_HMM",iter_dir)):
			os.makedirs(os.path.join(project_dir,"DENOGAP_HMM",iter_dir))
			self.iterdir_dict["ITERATION"]=os.path.join(project_dir,"DENOGAP_HMM",iter_dir)
		else:
			print "Can't over-write existing iteration directory at {0}\n".format(
				os.path.join(project_dir,"DENOGAP_HMM",iter_dir))
			print "Terminating Process\n"
			sys.exit()     
			                                                                  	
		if not os.path.exists(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"ALL_MATCH")):
			os.makedirs(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"ALL_MATCH"))
		self.iterdir_dict["ALL_MATCH"]=os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"ALL_MATCH")
	
		if not os.path.exists(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"BEST_MATCH")):
			os.makedirs(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"BEST_MATCH"))
		self.iterdir_dict["BEST_MATCH"]=os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"BEST_MATCH")
	
		if not os.path.exists(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"PARTIAL_MATCH")):
			os.makedirs(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"PARTIAL_MATCH"))
		self.iterdir_dict["PARTIAL_MATCH"]=os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"PARTIAL_MATCH")
		
		if not os.path.exists(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"CHIMERA_MATCH")):
			os.makedirs(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"CHIMERA_MATCH"))
		self.iterdir_dict["CHIMERIC_MATCH"]=os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"CHIMERA_MATCH")
		
		if not os.path.exists(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"CLUSTER")):
			os.makedirs(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"CLUSTER"))
		self.iterdir_dict["CLUSTER"]=os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"CLUSTER")
		
		if not os.path.exists(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"SUMMARY")):
			os.makedirs(os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"SUMMARY"))
		self.iterdir_dict["SUMMARY"]=os.path.join(project_dir,"DENOGAP_HMM",iter_dir,"SUMMARY")
		
		
		return(self.iterdir_dict)	
		
		
			
	
	
		
	
		
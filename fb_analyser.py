import zipfile
import tarfile
import gzip
import argparse
import shutil
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout, write_dot
import urllib.request
from urllib.parse import urlparse


def download(url, to=None):
	if to == None:
		file_name = urlparse(url).path.split('/')[-1]
	else:
		file_name = to + urlparse(url).path.split('/')[-1]
	with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
	return file_name
		
def unpack(file):
	if file.endswith('.zip') :
		with zipfile.ZipFile(file, 'r') as zip_ref:
			zip_ref.extratall()
	elif file.endswith('.tar.gz') or file.endswith('.tgz') :
		with tarfile.open(file, 'r:gz') as tar_ref:

import os

def is_within_directory(directory, target):
	
	abs_directory = os.path.abspath(directory)
	abs_target = os.path.abspath(target)

	prefix = os.path.commonprefix([abs_directory, abs_target])
	
	return prefix == abs_directory

def safe_extract(tar, path=".", members=None, *, numeric_owner=False):

	for member in tar.getmembers():
		member_path = os.path.join(path, member.name)
		if not is_within_directory(path, member_path):
			raise Exception("Attempted Path Traversal in Tar File")

	tar.extractall(path, members, numeric_owner=numeric_owner) 
	

safe_extract(tar_ref)
		#tar_ref = tarfile.open
	elif file.endswith('.txt.gz'):
		with gzip.open(file, 'r') as tar_ref:
			with open('dataset.txt', 'wb') as f_out:
				shutil.copyfileobj(tar_ref, f_out)
				
				
def prepData(src = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'):
	unpack(download(src))			

def analyze(datafile = 'dataset.txt'):
	G = nx.read_edgelist(datafile)
	nx.draw(G)
	print(nx.info(G))

def topTen():
	G = nx.read_edgelist(datafile)
	nx.draw(G)
	print(nx.info(G))

if __name__ == '__main__':
	prepData()
	prepData(src='https://snap.stanford.edu/data/facebook.tar.gz')
	analyze()
	
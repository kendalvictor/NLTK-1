from urllib import request
import nltk, re, pprint
from nltk import word_tokenize


url = "http://www.gutenberg.org/files/2554/2554.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
type(raw)


# 14976 - Mob Rule in New Orleans by Ida B. Wells-Barnett
# 02760 - Celebrated Crimes (Complete) by Alexandre Dumas
# 15803 - Crime and Its Causes by William Douglas Morrison
# 27523 - Masterpieces of Mystery in Four Volumes: Detective Stories by Joseph Lewis French
# 17866 - Murder in the Gunroom by H. Beam Piper
# 13097 - Lives of the Most Remarkable Criminals Who have been Condemned and Executed for
# 00477 - Criminal Sociology by Enrico Ferri
# 00466 - A Book of Remarkable Criminals by H. B. Irving
# 13172 - True Stories of Crime From the District Attorney's Office by Arthur Cheney Train
# 33922 - True Detective Stories from the Archives of the Pinkertons by Cleveland Moffett
# 17959 - The Hand Of Fu-Manchu by Sax Rohmer
# 11544 - The Crimes of England by G. K. Chesterton
# 22747 - Financial Crime and Corruption by Samuel Vaknin
# 05268 - Courts and Criminals by Arthur Cheney Train
# 46846 - Mysteries of Police and Crime by Arthur Griffiths
# 49230 - The History and Romance of Crime, Millbank Penitentiary by Griffiths
# 06628 - The Life, Crime, and Capture of John Wilkes Booth by George Alfred Townsend
# 01420 - London's Underworld by Thomas Holmes
# 27732 - City Crimes; Or, Life in New York and Boston by George Thompson
# 40348 - The Crime and the Criminal by Richard Marsh

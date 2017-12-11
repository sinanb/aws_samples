import boto3
from argparse import ArgumentParser

def get_args():
	parser = ArgumentParser(description='Call Compare Faces')
	parser.add_argument('-s', '--source')
	parser.add_argument('-t', '--target')
	return parser.parse_args()

# the rekognition service is available in eu-west-1
if __name__ == "__main__":
	session_args = get_args()
	# print(session_args.source)
	with open(session_args.source, "rb") as image_file:
		source_bytes = image_file.read()

	with open(session_args.target, "rb") as image_file:
		target_bytes = image_file.read()

	client = boto3.client('rekognition')

	response = client.compare_faces(
		SimilarityThreshold=2,
		SourceImage={
			'Bytes': target_bytes,
		},
		TargetImage={
			'Bytes': source_bytes,
		},
	)
	# print(response)
	for face_match in response["FaceMatches"]:
		print("Similarity level of the two faces is", face_match["Similarity"])
		print("Confidence of this similarity level is ", face_match["Face"]["Confidence"])
		
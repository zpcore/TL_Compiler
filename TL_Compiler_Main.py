from TL_Compiler import *



def main():
	MTL = "G[3](G[2]a0) & G[2]a0 &(a1 U[2]a2)" 

	parser.parse(MTL)
	#TLparse.optimize() # Comment this line to see unoptimized code
	TLparse.gen_assembly()


if __name__ == "__main__":
	main()
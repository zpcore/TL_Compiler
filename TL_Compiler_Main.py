from TL_Compiler import *



def main():
	MTL = "G[3](G[2]a0) & G[2]a0 & a1" 
	#MTL = "a0&a1&a3" 
	top_node = parser.parse(MTL)
	TLparse.optimize()


if __name__ == "__main__":
	main()
import argparse

from coin.fair_coin import run_fair_coin
from coin.biased_coin import run_biased_coin
from die.quantum_die import run_quantum_die
parser = argparse.ArgumentParser()
parser.add_argument("--mode",choices=["fair","biased","die"],  required=True)
parser.add_argument("--bias",type=float,default=70)
parser.add_argument("--shots", type=int,default=1024)
parser.add_argument("--sides",type=int,default=6)
args = parser.parse_args()
if args.mode=="fair":
    run_fair_coin(args.shots)
elif args.mode=="biased":
    run_biased_coin(args.bias,args.shots)
elif args.mode=="die":
    run_quantum_die(args.sides,args.shots)
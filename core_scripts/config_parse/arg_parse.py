#!/usr/bin/env python
"""
config_parse

Argument parse

"""
from __future__ import absolute_import

import os
import sys
import argparse

import core_scripts.other_tools.list_tools as nii_list_tools
import core_scripts.other_tools.display as nii_display

__author__ = "Xin Wang"
__email__ = "wangxin@nii.ac.jp"
__copyright__ = "Copyright 2020, Xin Wang"



#############################################################
# argparser
#
def f_args_parsed(argument_input = None):

    # Training settings
    parser = argparse.ArgumentParser(description='General argument parse')

    
    parser.add_argument('--batch-size', type=int, \
                        default=64, metavar='N', \
                        help='input batch size for training (default: 64)')
        
    parser.add_argument('--epochs', type=int, \
                        default=50, metavar='N', \
                        help='number of epochs to train (default: 50)')
    
    parser.add_argument('--no-best-epochs', type=int, \
                        default=5, metavar='N', \
                        help='number of no-best epochs before stop training (default: 5)')
    
    parser.add_argument('--lr', type=float, \
                        default=0.0001, metavar='LR', \
                        help='learning rate (default: 0.0001)')
    
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='disables CUDA training')
    
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')

    # options to save model / checkpoint
    parser.add_argument('--save-model-dir', type=str, \
                        default="./", \
                        help='save model to this direcotry (default: ./)')
        
    parser.add_argument('--not-save-each-epoch', \
                        action='store_true', default=False,
                        help='not save model after each epoch (default: False)')
    
    parser.add_argument('--save-epoch-name', type=str, \
                        default="epoch", \
                        help='name prefix of saved model (default: epoch)')

    parser.add_argument('--save-trained-name', type=str, \
                        default="trained_network", \
                        help='name of trained model (default: trained_network)')
    
    parser.add_argument('--save-model-ext', type=str, \
                        default=".pt",
                        help='extension name of model (default: .pt)')

    # options to output
    parser.add_argument('--output-dir', type=str, \
                        default="./output", \
                        help='path to save generated data (default: ./output)')
    
    parser.add_argument('--optimizer', type=str, \
                        default='Adam', metavar='str',
                        help='which optimizer to use (Adam | SGD, default: Adam)')

    parser.add_argument('--verbose', type=int, \
                        default=1, metavar='N',
                        help='verbose level 0: nothing, 1:print error per utterance (default: 1)')

    
    if argument_input is not None:
        return parser.parse_args(argument_input)
    else:
        return parser.parse_args()


if __name__ == "__main__":
    pass
    

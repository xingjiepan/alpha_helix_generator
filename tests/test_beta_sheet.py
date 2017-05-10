#!/usr/bin/env python3

import pytest
import numpy as np
np.seterr(all='raise')

import ss_generator as ssg


def test_build_beta_sheet():
    print("test build beta sheet.")
    
    res_list = ssg.beta_sheet.build_ideal_flat_beta_sheet('parallel', 10, 5)
    ssg.IO.save_residue_list(res_list, "ideal_flat_sheet.pdb")

    ssg.basic.change_torsions(res_list[1], 5, np.radians(-120), np.radians(120))
    ssg.IO.save_residue_list(res_list, "perturbed_sheet.pdb")

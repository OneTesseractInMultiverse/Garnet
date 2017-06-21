#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import string
import hashlib


# ------------------------------------------------------------------------------
# FUNCTION GEN_SALT
# ------------------------------------------------------------------------------
# Generates a random
def gen_salt(length):
    return ''.join(random.SystemRandom()
                   .choice(string.ascii_uppercase + string.digits) for _ in range(length))


# --------------------------------------------------------------------------
# METHOD __COMPUTE_HASH
# --------------------------------------------------------------------------
# Computes the SHA256 hash of the given password and encodes the result into
# a hexadecimal string.
def compute_hash(password, salt):
    return hashlib.sha256(password.encode('utf-8')+salt.encode('utf-8'))\
        .hexdigest()

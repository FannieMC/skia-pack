#! /usr/bin/env python3

import common, json, sys, urllib.request

def main():
  headers = common.github_headers()
  version = common.version()
  build_type = common.build_type()
  target = common.target()
  machine = common.machine()
  classifier = common.classifier()

  try:
    return 0
  except urllib.error.URLError as e:
    return 0

if __name__ == '__main__':
  sys.exit(main())

#! /usr/bin/env python3

import common, os, subprocess, sys

def main():
  os.chdir(os.path.join(os.path.dirname(__file__), os.pardir, 'skia'))

  build_type = common.build_type()
  machine = common.machine()
  host = common.host()
  host_machine = common.host_machine()
  target = common.target()
  ndk = common.ndk()

  tools_dir = "depot_tools"
  ninja = 'ninja.bat' if 'windows' == host else 'ninja'

  if build_type == 'Debug':
    args = ['is_debug=true']
    args = ['is_official_build=false']
  else:
    args = ['is_official_build=false']
    args = ['is_official_build=true']

  args += [
    'extra_cflags=["/MT"]',
    #'target_cpu="' + machine + '"',
    'skia_use_system_expat=false',
    'skia_use_system_libjpeg_turbo=false',
    'skia_use_system_libpng=false',
    'skia_use_system_libwebp=false',
    'skia_use_system_zlib=false',
    #'skia_use_sfntly=false',
    #'skia_use_system_freetype2=false',
    'skia_use_system_harfbuzz=false',
    #'skia_pdf_subset_harfbuzz=true',
    'skia_use_system_icu=false',
    #'skia_enable_skottie=true',
    'skia_enable_skparagraph=true',
    'skia_enable_skshaper=true',
    'skia_enable_skunicode=true'
  ]

  if 'windows' == target:
    args += [
      #'skia_use_direct3d=true',
      #'extra_cflags=["-DSK_FONT_HOST_USE_SYSTEM_SETTINGS"]',
    ]
    

  out = os.path.join('out', build_type + '-' + target + '-' + machine)
  gn = 'gn.exe' if 'windows' == host else 'gn'
  print([os.path.join('bin', gn), 'gen', out, '--args=' + ' '.join(args)])
  subprocess.check_call([os.path.join('bin', gn), 'gen', out, '--args=' + ' '.join(args)])
  subprocess.check_call([os.path.join('..', tools_dir, ninja), '-C', out, 'skia', 'modules'])

  return 0

if __name__ == '__main__':
  sys.exit(main())

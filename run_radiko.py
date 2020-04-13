import os
import argparse
from datetime import datetime, timedelta, timezone
import logging
from record import record
from post_slack import post_slack


def _get_args():
    parser = argparse.ArgumentParser(description='record radiko')
    parser.add_argument('station',
     type=str,
     help='radiko station')
    parser.add_argument('program',
     type=str,
     help='radiko program name')
    parser.add_argument('recordtime',
     type=int,
     help='recording time.(unit:miniutes)')
    parser.add_argument('-u', '--uploadgcloud',
     type=bool,
     help='upload recorded file to gcloud storage')
    args = parser.parse_args()
    return args.station, args.program, args.recordtime, args.uploadgcloud


if __name__ == "__main__":
    post = False
    if post:
        post_slack("自動ポスト","Start")

    cwd = os.getcwd()
    if not os.path.isdir(os.path.join(cwd, ".log")):
            os.mkdir(os.path.join(cwd, ".log"))
    if not os.path.isdir(os.path.join(cwd, "tmp")):
            os.mkdir(os.path.join(cwd, "tmp"))

    # ログ設定をする
    logging.basicConfig(filename=os.path.join(cwd, '.log/record_radiko.log'), level=logging.DEBUG)
    # 実行時パラメータを取得する
    station, program, rtime, uploads = _get_args()

    JST = timezone(timedelta(hours=+9), 'JST')
    current_time = datetime.now(tz=JST).strftime("%Y%m%d_%H%M")
    logging.debug(f'current time: {current_time}, \
        station: {station}, \
        program name: {program}, \
        recording time: {rtime}, \
        uploads: {uploads}')
    # 録音保存先を用意する
    outfilename = os.path.join(cwd, f'tmp/{current_time}_{station}_{program}.aac')
    logging.debug(f'outfilename:{outfilename}')
    # 録音
    record(station, program, rtime, outfilename)
    if post:
        # 終了の通知
        post_slack("自動ポスト","Done")


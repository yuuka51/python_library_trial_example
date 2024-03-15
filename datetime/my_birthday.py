"""
誕生日を使用してdatetimeの操作を行う。
やりたいこと
- 自分が生後何日か出力する
- 自分が生後何か月か出力する
- 応用として、小学何年生か、中学何年生か、高校何年生か、大学何年生か出力してみる
"""

from datetime import datetime

from dateutil.relativedelta import relativedelta


def my_birthday(birthday):
    """
    誕生日をもとに生後何日か、生後何か月か出力する関数
    :param birthday: 誕生日
    :return:
    :rtype: None
    :Example:
    >>> my_birthday(datetime(○○○○, ○○, ○))
    あなたは生後○○○日です
    あなたは生後○○ヶ月です
    """
    # 生後何日
    how_many_days_old = datetime.now() - birthday
    print("あなたは生後" + str(how_many_days_old.days) + "日です")
    # 生後何ヶ月
    how_many_old_relativedelta = relativedelta(datetime.now(), birthday)
    how_many_months_old = (
        how_many_old_relativedelta.years * 12
    ) + how_many_old_relativedelta.months
    print("あなたは生後" + str(how_many_months_old) + "ヶ月です")
    # もし入力された日と今日が同じ月と同じ日だったら誕生日おめでとうと出力する
    if birthday.month == datetime.now().month and birthday.day == datetime.now().day:
        print("誕生日おめでとうございます！")


def main():
    print("あなたの生年月日から生後経過日数や生後経過月数を計算します。")
    print("西暦何年生まれですか？")
    year = int(input())
    print("何月生まれですか？")
    month = int(input())
    print("何日生まれですか？")
    day = int(input())
    my_birthday(datetime(year, month, day))
    my_birthday(datetime(1997, 3, 15))


if __name__ == "__main__":
    main()

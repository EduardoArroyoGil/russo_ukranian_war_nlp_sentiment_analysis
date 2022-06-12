
class TwitterUtils:

    pass

    def check_correct_acc_tw_association(self, account_id_1, account_id_2):

        if account_id_1 == account_id_2:
            return True
        else:
            return False

    def align_column_raw_types_to_insert(self,df):

        all_columns = df.columns

        df[all_columns] = df[all_columns].astype(str)

        type_columns = {
            'account_id': 'int',
            'account_id_check': 'int',
            'tweet_id': 'int',
            'account_username': 'str',
            'account_name': 'str',
            'tweet_text': 'str',
            'tweet_created_at': 'datetime64[ns]',
            'tweet_language': 'str',
            'retweet_count': 'int',
            'reply_count': 'int',
            'like_count': 'int',
            'quote_count': 'int',
            'profile_image_url': 'str',
            'is_reclaimable': 'bool'
        }

        df = df.astype(type_columns)

        return df
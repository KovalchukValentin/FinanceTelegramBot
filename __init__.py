import os
import keys
import telebot

# {'content_type': 'text', 'id': 16, 'message_id': 16, 'from_user': {'id': 6683159831, 'is_bot': False, 'first_name': 'Valentin', 'username': 'valentinkovalchuk', 'last_name': 'Kovalchuk', 'language_code': 'en', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None}, 'date': 1699457482, 'chat': {'id': 6683159831, 'type': 'private', 'title': None, 'username': 'valentinkovalchuk', 'first_name': 'Valentin', 'last_name': 'Kovalchuk', 'is_forum': None, 'photo': None, 'bio': None, 'join_to_send_messages': None, 'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None, 'active_usernames': None, 'emoji_status_custom_emoji_id': None, 'has_hidden_members': None, 'has_aggressive_anti_spam_enabled': None, 'emoji_status_expiration_date': None}, 'sender_chat': None, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': 'f', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'message_thread_id': None, 'is_topic_message': None, 'forum_topic_created': None, 'forum_topic_closed': None, 'forum_topic_reopened': None, 'has_media_spoiler': None, 'forum_topic_edited': None, 'general_forum_topic_hidden': None, 'general_forum_topic_unhidden': None, 'write_access_allowed': None, 'user_shared': None, 'chat_shared': None, 'story': None, 'json': {'message_id': 16, 'from': {'id': 6683159831, 'is_bot': False, 'first_name': 'Valentin', 'last_name': 'Kovalchuk', 'username': 'valentinkovalchuk', 'language_code': 'en'}, 'chat': {'id': 6683159831, 'first_name': 'Valentin', 'last_name': 'Kovalchuk', 'username': 'valentinkovalchuk', 'type': 'private'}, 'date': 1699457482, 'text': 'f'}}
BOT_TOKEN = os.environ["FINANCE_BOT_TOKEN"]
MONOBANK_TOKEN = os.environ["MONOBANK_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)
users_ids = [6683159831, 384240259]


def isMessageCorrect(message):
    pass


class TransactionData:
    def __init__(self, value, group, comment):
        self.value = value
        self.group = group
        self.comment = comment

    def __str__(self):
        return f'TransactionData(value = {self.value}, group = {self.group}, comment = {self.comment})'


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "What are you doing here?")


@bot.message_handler(commands=['template'])
def send_template(message):
    if not message.from_user.id in users_ids:
        bot.reply_to(message, "No authorization")
        return
    bot.reply_to(message, "Value\nGroup\nComment")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    if not message.from_user.id in users_ids:
        bot.reply_to(message, "No authorization")
        return
    text = message.text.split("\n")


if __name__ == "__main__":
    bot.infinity_polling()
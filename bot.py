import os
import logging
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MAIN_MENU = [
    ["🏛️ عن الكلية", "💻 التخصصات"],
    ["📚 المواد الدراسية", "🛠️ أدوات الطالب"],
    ["📖 أدوات الدراسة", "🎓 نصائح للطلاب"],
    ["❓ الأسئلة الشائعة", "🔗 روابط مهمة"]
]

BACK = "🔙 رجوع"
HOME = "🏠 القائمة الرئيسية"


def keyboard(rows):
    return ReplyKeyboardMarkup(
        rows + [[BACK, HOME]],
        resize_keyboard=True
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text(
        "🎓 مرحباً بك في CSIT Guide!\n\n"
        "دليلك للتعرف على كلية علوم الحاسوب "
        "وتقانة المعلومات بجامعة سنار.\n\n"
        "اختر القسم الذي تريد استكشافه:",
        reply_markup=keyboard(MAIN_MENU)
    )


async def show_main(update: Update):
    await update.message.reply_text(
        "🏠 القائمة الرئيسية\nاختر القسم:",
        reply_markup=keyboard(MAIN_MENU)
    )


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip()

    if msg == HOME:
        context.user_data.clear()
        await show_main(update)
        return

    if msg == BACK:
        await show_main(update)
        return

    if msg == "🏛️ عن الكلية":
        await update.message.reply_text(
            "🏛️ كلية علوم الحاسوب وتقانة المعلومات\n"
            "جامعة سنار.\n\n"
            "تهتم بعلوم الحاسوب وتقانة المعلومات "
            "والبحث العلمي والتطبيق العملي.\n\n"
            "للمعلومات الرسمية:\nhttps://uofs.edu.sd/"
        )
        return

    if msg == "💻 التخصصات":
        await update.message.reply_text(
            "💻 مجالات الدراسة:\n\n"
            "• علوم الحاسوب\n"
            "• تقانة المعلومات\n"
            "• نظم المعلومات\n"
            "• شبكات الحاسوب\n\n"
            "يرجى الرجوع للجامعة لتأكيد البرامج "
            "المتاحة حالياً."
        )
        return

    if msg == "📚 المواد الدراسية":
        await update.message.reply_text(
            "📚 المستوى الأول - الفصل الأول:\n\n"
            "1. الثقافة الإسلامية\n"
            "2. مبادئ الفيزياء\n"
            "3. الحسبان (التفاضل والتكامل)\n"
            "4. English Skills 1\n"
            "5. الرياضيات المتقدمة\n"
            "6. اللغة العربية\n"
            "7. أساسيات الحاسوب\n\n"
            "هذه القائمة مقدمة من طالب، "
            "وتحتاج إلى مطابقة الخطة الرسمية."
        )
        return

    if msg == "🛠️ أدوات الطالب":
        await update.message.reply_text(
            "🛠️ أدوات الطالب:\n\n"
            "🧮 الحاسبة العلمية: استخدم حاسبة هاتفك.\n"
            "📅 تنظيم المهام: اكتب مهامك اليومية.\n"
            "📝 تدوين الملاحظات: استخدم Google Keep.\n"
            "📊 حساب المعدل: ستضاف حاسبة تفاعلية لاحقاً."
        )
        return

    if msg == "📖 أدوات الدراسة":
        await update.message.reply_text(
            "📖 مصادر مفيدة:\n\n"
            "🐍 Python:\nhttps://www.python.org/\n\n"
            "💻 تعلم البرمجة:\nhttps://www.freecodecamp.org/\n\n"
            "🇬🇧 الإنجليزية:\nhttps://www.bbc.co.uk/learningenglish\n\n"
            "📄 ملفات PDF:\nhttps://www.ilovepdf.com/"
        )
        return

    if msg == "🎓 نصائح للطلاب":
        await update.message.reply_text(
            "🎓 نصائح دراسية:\n\n"
            "1. راجع محاضراتك باستمرار.\n"
            "2. طبّق البرمجة بنفسك.\n"
            "3. قسّم المهام الكبيرة إلى أجزاء صغيرة.\n"
            "4. لا تؤجل الاستعداد للامتحانات.\n"
            "5. اهتم بالمشاريع العملية."
        )
        return

    if msg == "❓ الأسئلة الشائعة":
        await update.message.reply_text(
            "❓ الأسئلة الشائعة:\n\n"
            "كيف أبدأ البرمجة؟\n"
            "ابدأ بلغة Python وتعلم الأساسيات.\n\n"
            "أين أجد معلومات الجامعة؟\n"
            "https://uofs.edu.sd/\n\n"
            "أين أجد منصة التعليم الإلكتروني؟\n"
            "https://e-learning.uofs.edu.sd/"
        )
        return

    if msg == "🔗 روابط مهمة":
        await update.message.reply_text(
            "🔗 الموقع الرسمي:\nhttps://uofs.edu.sd/\n\n"
            "📚 التعليم الإلكتروني:\n"
            "https://e-learning.uofs.edu.sd/?lang=ar"
        )
        return

    await update.message.reply_text(
        "اختر أحد الأزرار الموجودة في القائمة الرئيسية.",
        reply_markup=keyboard(MAIN_MENU)
    )


async def error_handler(update, context):
    logger.error("حدث خطأ أثناء معالجة الطلب", exc_info=context.error)


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, answer)
    )
    app.add_error_handler(error_handler)

    logger.info("CSIT Guide Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()

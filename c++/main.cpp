#include <QApplication>
#include <QLabel>
#include <QWidget>
int main(int argc, char *argv[ ]) {
    QApplication app(argc, argv);
    QLabel hello("Hello World");
    hello.setWindowTitle("PONG");
    hello.resize(800, 600);
    hello.show();
    return app.exec();
}

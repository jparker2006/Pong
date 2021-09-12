#include <QApplication>
#include <QLabel>
#include <QWidget>
int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QLabel hello("PONG");
    hello.setWindowTitle("Pong");
    hello.resize(600,400);
    hello.show();
    return app.exec();
}

#include "lists.h"
/*
*insert_node -  inserts a number into a sorted singly linked list.
*@head: A pointer to the head of the dlistint_t list.
*@number: the number to insert
*Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newnode, *node = *head;

    newnode = malloc(sizeof(listint_t));
    if (newnode == NULL)
        return (NULL);
    newnode->n = number;

    if (node == NULL || node->n >= number)
    {
        newnode->next = node;
        *head = newnode;
        return (newnode);
    }
    while (node && node->next && node->next->n < number)
        node = node->next;
    newnode->next = node->next;
    node->next = newnode;

    return (newnode);
}